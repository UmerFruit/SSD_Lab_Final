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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install flask
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    echo 'Running unit tests...'
                    python -m unittest test_app.py
                '''
            }
        }
        
        stage('Build Application') {
            steps {
                sh '''
                    . venv/bin/activate
                    echo 'Building application...'
                    echo 'Flask app is ready for deployment'
                '''
            }
        }
        
        stage('Deploy Application') {
            steps {
                sh '''
                    . venv/bin/activate
                    echo 'Deploying application...'
                    mkdir -p /tmp/deployment
                    cp -r * /tmp/deployment/
                    echo 'Application deployed to /tmp/deployment'
                '''
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
