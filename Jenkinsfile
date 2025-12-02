pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                sh 'echo "Build step goes here"'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo "Run tests here"'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh 'echo "Deploy step goes here"'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
