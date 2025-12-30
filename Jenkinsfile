pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/UmerFruit/SSD_Lab_Final'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install flask'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                echo 'No tests defined yet - tests would run here'
            }
        }
        
        stage('Build Application') {
            steps {
                echo 'Building application...'
                echo 'Flask app is ready for deployment'
            }
        }
        
        stage('Deploy Application') {
            steps {
                echo 'Deploying application...'
                sh 'mkdir -p /tmp/deployment'
                sh 'cp -r * /tmp/deployment/'
                echo 'Application deployed to /tmp/deployment'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
