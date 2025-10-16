pipeline {
    agent {
        node {
            label 'local'
            customWorkspace 'C:\\College Files\\MLOPS\\P5\\git_remote'
        }
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub repository...'
                git branch: 'main', url: 'https://github.com/tathya1001/jenkins-test.git'
            }
        }

        stage('Show Workspace') {
            steps {
                echo 'Showing current workspace directory...'
                bat 'cd'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images for webapp and dbapp...'
                bat 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests to run, skipping...'
            }
        }

        stage('Deploy Containers') {
            steps {
                echo 'Starting services using Docker Compose...'
                bat 'docker-compose up -d'
            }
        }

        stage('Verify Running Containers') {
            steps {
                echo 'Listing running containers...'
                bat 'docker ps'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            // bat 'docker-compose down'   // uncomment if you want to cleanup
        }
    }
}
