pipeline {
    options {
           skipStagesAfterUnstable()
    }
    agent {dockerfile true}
    stages {

        stage('Build') {
            steps {
                sh 'python3 -m py_compile SeleniumProject/masterSelenium/selenium_get.py'
            }
        }
        stage('Tests') {
            steps {
                sh 'python3 SeleniumProject/masterSelenium/selenium_get.py'
            }
        }
    }
}