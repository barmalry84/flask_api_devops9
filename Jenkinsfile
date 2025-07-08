pipeline {
    agent { label 'agent-1' }
    
    environment {
        AWS_REGION = 'eu-west-1'
        ECR_REPO = 'flask-api'
        AWS_ACCOUNT_ID = '381492243289'
        URL_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE_TAG = "${URL_REGISTRY}/${ECR_REPO}"
        RUNNER_CONTAINER = 'test_runner'
    }

    stages { 

        // 1. Checkout from SCM (Git)
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/barmalry84/flask_api_devops9'
            }
        }
        
        // 2. Build Docker Containers with Docker Compose
        stage('Docker Compose Build') {
            steps {
                script {
                    // Build and run containers using                     
                    sh """
                        echo "Running docker compose uat tests for flask api"
                        echo "----------------------------------------------"
                        docker compose stop
                        docker compose build --no-cache
                        docker compose up --abort-on-container-exit --exit-code-from $RUNNER_CONTAINER
                        echo "Tests are finished"
                        docker compose stop
                    """
                }
            }
        }
        
        // 3. Build Flask Docker Image
        stage('Build Flask Image') {
            steps {
                script {
                    // Build Flask image from Dockerfile
                    sh 'docker build -t flask-app:latest ./flask_api'
                }
            }
        }

        // 4. Push Flask Image to ECR
        stage('Push Image to ECR') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'ECR-Access', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                        
                        // AWS ECR login
                        sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${URL_REGISTRY}"
                        
                        // Tag the image
                        sh "docker tag flask-app:latest \"${IMAGE_TAG}:latest\""
                        
                        // Push to ECR
                        sh "docker push \"${IMAGE_TAG}:latest\""
                    }
                }
            }
        }

        // 5. Run Flask Container from ECR
        stage('Deploy image to EC2') {
            agent { label 'agent-2' }
            steps {
                script {
                    sh """
                    docker stop flask-container && docker rm flask-container
                    docker run -d --name flask-container \
                        -p 5010:5010 \
                        \"${IMAGE_TAG}:${GIT_COMMIT}\"
                    """
                }
            }
        }
        
    }

}