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
        stage('Language response search') {
            steps {
                sh 'python3 SeleniumProject/masterSelenium/selenium_language_search_response_test.py'
            }
        }
        stage('Display person ETH DB') {
            steps {
                sh 'python3 SeleniumProject/masterSelenium/selenium_display_person_eth_db.py'
            }
        }
    }
}