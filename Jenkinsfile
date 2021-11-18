pipeline {
      agent any
      stages {
            stage('Clone') {
                  steps {
                        git 'https://github.com/dongsinhho/WebDjango.git'
                  }
            }
            stage('Build') {
                  steps {
                        sh "echo Build Ho Ngoc Dong Sinh"
                  }
            }
            stage('Test') {
                  steps {
                        sh "echo Test Ho Ngoc Dong Sinh"
                  }
            }
      }
}
