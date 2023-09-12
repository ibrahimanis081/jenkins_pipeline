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
        sh 'python3 -m venv venv'
        sh 'source venv/bin/activate'
        sh 'cd app'
        sh 'ls -la'
        sh 'pip install -r requirements.txt'
        sh 'python3 test_app.py'
        sh 'deactivate'
      }
    }

  }
}