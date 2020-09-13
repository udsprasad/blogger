pipeline {
    agent any 
    stages {
        stage('Test') { 
            steps {
                slackSend channel: 'web-blogger', color: 'good', message: 'Unit & Funtional Test_Case started.'
                sh label: '', script: '''cd Blogger
                python3 -m coverage run --source tests,project,config -m  pytest -v
                python3 -m coverage xml -i
                cd ../selenium
                python3 test_login.py'''
            }
            post { 
                success { 
                        slackSend channel: 'web-blogger', color: 'good', message: 'successful completed Unit & Functional Test_Case stage'
                        }   
                failure {
                          slackSend channel: 'web-blogger', color: 'danger', message: ' failed Unit Test_Case stage'
                        }
            }
            
        }
        stage('SonarQube analysis and created zip file') {
               environment {
                            scannerHome= tool name: 'SonarQube Scanner 3.0.2.768', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                           } 
            steps {
                  withSonarQubeEnv("Scan") {
                      slackSend channel: 'web-blogger', color: 'good', message: 'SonarQube stage started.'
                      sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=Project -Dsonar.projectName=Blogger${BUILD_NUMBER} -Dsonar.projectVersion=1.0 -Dsonar.sources=Blogger/project/ -Dsonar.exclusions=**/*.html,**/*.css,**/*.js -Dsonar.sourceEncoding=UTF-8 -Dsonar.python.coverage.reportPath=Blogger/coverage.xml '''
                  }
                 sh label: '', script: ' zip Blogger.zip -r Blogger'
            }
             post { 
               success { 
                        slackSend channel: 'web-blogger', color: 'good', message: 'successful completed SonarQube analysis & zip creation stage'
                       }     
               failure {
                        slackSend channel: 'web-blogger', color: 'danger', message: ' failed SonarQube analysis & zip creation stage'
                       }
             }
         }
         stage('Jfrog_upload') { 
            steps {
                 slackSend channel: 'web-blogger', color: 'good', message: 'Jfrog stage started.'
                 sh label: '', script: 'curl -uadmin:admin@123 -T *.zip "http://localhost:8083/artifactory/Artifacts_repo_pipeline/Capstone_${BUILD_NUMBER}/"'
            }
            post {
                success { 
                          slackSend channel: 'web-blogger', color: 'good', message: 'successful completed Jfrog_upload stage'
                        }          
                failure {
                          slackSend channel: 'web-blogger', color: 'danger', message: ' failed Jfrog_upload stage'
                        }
            }
        }
         stage('Deploy') { 
            steps {
                slackSend channel: 'web-blogger', color: 'good', message: 'Deploy stage started.'
                ansiblePlaybook installation: 'ansible', playbook: 'docker.yml'
            }
             post { 
               success { 
                        slackSend channel: 'web-blogger', color: 'good', message: 'successful completed Deploy stage'
                       }                 
               failure {
                        slackSend channel: 'web-blogger', color: 'danger', message: ' failed Deploy stage'
                       }
            }
        }        
    }   
 // Post-build Slack Notification action
post { 
    success {
                slackSend channel: 'web-blogger', color: 'good', message: " Successfully Completed :'${env.JOB_NAME}' Build Number: '${env.BUILD_NUMBER}' Build URL: '(<${env.BUILD_URL}|Open>)'"
            }                
    failure {
                slackSend channel: 'web-blogger', color: 'danger', message: " Failed :'${env.JOB_NAME}' Build Number: '${env.BUILD_NUMBER}' Build URL: '(<${env.BUILD_URL}|Open>)'"
            }
    }
}
