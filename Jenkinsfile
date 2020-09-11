pipeline {
    agent any 
    stages {
        stage('Test') { 
            steps {
                sh label: '', script: '''cd Blogger
                python3 -m coverage run -m  pytest -v
                python3 -m coverage xml -i
                cd ../selenium
                python3 test_login.py
                zip Blogger.zip -r Blogger'''
            }
        }
        stage('SonarQube analysis') {
             steps {
                  script {
                  def scannerHome = tool 'SonarQube Scanner 3.0.2.768';
                  withSonarQubeEnv("Scan") {
                   sh "${scannerHome}/bin/sonar-scanner"
                  }
              }
           }
         }
         stage('Deploy') { 
            steps {
                ansiblePlaybook installation: 'ansible', playbook: 'docker.yml'
            }
        }
    }
}
