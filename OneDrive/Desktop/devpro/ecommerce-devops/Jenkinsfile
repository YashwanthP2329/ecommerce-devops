pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/YashwanthP2329/ecommerce-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ecommerce-app .'
            }
        }
    }
}