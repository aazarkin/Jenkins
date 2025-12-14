pipeline {
    agent any

    environment {
        APP_NAME = "sandbox-hitcounter"
        IMAGE_NAME = "sandbox-hitcounter"
        APP_DIR = "/var/www/sandbox-dashboard/sandbox-app"
        DATA_VOLUME = "/var/www/sandbox-dashboard/sandbox-app/data:/data"
        HOST_PORT = "5001"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aazarkin/Jenkins.git', credentialsId: 'githubtoken'
  // replace with your repo
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    docker build -t ${IMAGE_NAME} ${APP_DIR}
                    """
                }
            }
        }

        stage('Stop Previous Container') {
            steps {
                script {
                    sh """
                    docker stop ${APP_NAME} || true
                    docker rm ${APP_NAME} || true
                    """
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker run -d -p ${HOST_PORT}:${CONTAINER_PORT} -v ${DATA_VOLUME} --name ${APP_NAME} ${IMAGE_NAME}
                    """
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    sh """
                    sleep 3  # wait for Flask to start
                    curl -f http://localhost:${HOST_PORT}/
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Jenkins pipeline completed successfully. App is running on port ${HOST_PORT}"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}
