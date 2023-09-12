pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ibrahimanis081/jenkins_pipeline.git', branch: 'main')
      }
    }
    
    stage('Test') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
                
                // Activate the virtual environment
                sh 'source venv/bin/activate'
                
                // Change to the app directory
                sh 'cd app'
                
                // List files to verify you're in the correct directory
                sh 'ls -la'
                
                // Install dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
                
                // Run your test script
                sh 'python3 test_app.py'
                
                // Deactivate the virtual environment
                sh 'deactivate'
            }
        }
    }
}