pipeline {
      agent none
      stages {
            stage('Clone') {
                  steps {
                        git 'https://github.com/dongsinhho/WebDjango.git'
                  }
            }
            stage('Build') {
                  agent {
                        docker {
                            image 'python:3.9' 
                        }
                  }
                  steps {
                        sh "pip install -r requirements.txt"
                        sh "echo Ho Ngoc Dong Sinh"
                  }
            }
      }
}
