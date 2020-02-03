pipeline {
    options {
           skipStagesAfterUnstable()
    }
    agent {dockerfile true}
    stages {

        stage('Build') {
            steps {
                sh 'python -m py_compile SeleniumProject/masterSelenium/selenium_get.py'
            }
        }
        stage('Test2') {
            steps {
                sh '--verbose --junit-xml test-reports/results.xml SeleniumProject/masterSelenium/selenium_get.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}