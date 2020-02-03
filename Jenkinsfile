pipeline {
    options {
           skipStagesAfterUnstable()
    }
    stages {

        stage('Build') {
            docker {
                image 'python:3.7-alpine'
            }
            steps {
                sh 'python -m py_compile SeleniumProject/masterSelenium/selenium_get.py'
            }
        }
        agent {dockerfile true}
        stage('Test2') {
            steps {
                sh 'python SeleniumProject/masterSelenium/selenium_get.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}