pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Lokeshwar9704/application.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('package.json')) {
                        sh 'npm install'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (fileExists('package.json')) {
                        sh 'npm test'
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'cp -r ./build/* /var/www/html'
                sh 'sudo systemctl restart nginx'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
