pipeline {
    agent any

    environment {
        IMAGE_NAME = "django-app"
        DOCKERHUB_USER = "reshma0209"   // 👈 ADD THIS
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    def tag = "${BUILD_NUMBER}"
                    sh "docker build -t $IMAGE_NAME:$tag ./studentproject"
                    sh "docker tag $IMAGE_NAME:$tag $IMAGE_NAME:latest"
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    def tag = "${BUILD_NUMBER}"

                    sh "docker tag $IMAGE_NAME:$tag $DOCKERHUB_USER/$IMAGE_NAME:$tag"
                    sh "docker tag $IMAGE_NAME:latest $DOCKERHUB_USER/$IMAGE_NAME:latest"

                    sh "docker push $DOCKERHUB_USER/$IMAGE_NAME:$tag"
                    sh "docker push $DOCKERHUB_USER/$IMAGE_NAME:latest"
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    def tag = "${BUILD_NUMBER}"
                    sh """
                    docker stop django-container || true
                    docker rm django-container || true
                    docker run -d -p 8000:8000 --name django-container $DOCKERHUB_USER/$IMAGE_NAME:$tag
                    """
                }
            }
        }
    }
}
