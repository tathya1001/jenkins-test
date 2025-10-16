pipeline {
    agent {
        node {
            label 'local'
            customWorkspace 'C:\\College Files\\MLOPS\\P5\\git_jenkins'
        }
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out code from local Git repository (same workspace)...'
                git branch: 'main', url: "file:///C:/College%20Files/MLOPS/P5/git_jenkins"
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
            echo 'Cleaning up containers after pipeline completion...'
            // bat 'docker-compose down'
        }
    }
}
