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
                        sh "pip install -r requirements.txt"
                  }
            }
      }
}
