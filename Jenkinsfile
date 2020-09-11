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
            tools {
               sonarQube 'SonarQube Scanner 3.0.2'
                 }
           steps {
            withSonarQubeEnv('SonarQube Scanner') {
             sh 'sonar-scanner'
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
