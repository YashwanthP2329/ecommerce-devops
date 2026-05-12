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
}pipeline {
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
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Testing Application'
            }
        }
    }
}