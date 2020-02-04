pipeline {
    options {
           skipStagesAfterUnstable()
    }
    agent {dockerfile true}
    stages {

        stage('Build') {
            steps {
                sh 'python3 -m py_compile SeleniumProject/masterSelenium/selenium_language_search_response_test.py SeleniumProject/masterSelenium/selenium_get2.py'
            }
        }
        stage('Test language response search') {
            steps {
                sh 'python3 SeleniumProject/masterSelenium/selenium_language_search_response_test.py'
            }
        }
        stage('Test ') {
            steps {
                sh 'python3 SeleniumProject/masterSelenium/selenium_get2.py'
            }
        }
    }
}