pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YashwanthP2329/ecommerce-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python --version'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Testing Application'
            }
        }
    }
}