pipeline {
    agent any 
    stages {
        stage('Test') { 
            steps {
                sh label: '', script: '''cd Blogger
                python3 -m coverage run --source tests,project,config -m  pytest -v
                python3 -m coverage xml -i
                cd ../selenium
                python3 test_login.py'''
            }
        }
        stage('SonarQube analysis and created zip file') {
               environment {
              scannerHome= tool name: 'SonarQube Scanner 3.0.2.768', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
             } 
             steps {
                  withSonarQubeEnv("Scan") {
                   sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=Project -Dsonar.projectName=Blogger${BUILD_NUMBER} -Dsonar.projectVersion=1.0 -Dsonar.sources=Blogger -Dsonar.exclusions=**/*.html,**/*.css,**/*.js -Dsonar.sourceEncoding=UTF-8 -Dsonar.python.coverage.reportPath=Blogger/coverage.xml '''
                  }
  
                 sh label: '', script: ' zip Blogger.zip -r Blogger'
           }
         }
         stage('Jfrog_upload') { 
            steps {
                 sh label: '', script: 'curl -uadmin:admin@123 -T *.zip "http://localhost:8083/artifactory/example-repo-local/Capstone_${BUILD_NUMBER}/"'
            }
        }
         stage('Deploy') { 
            steps {
                ansiblePlaybook installation: 'ansible', playbook: 'docker.yml'
            }
        }
    }
}
