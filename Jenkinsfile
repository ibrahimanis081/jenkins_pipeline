pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ibrahimanis081/jenkins_pipeline.git', branch: 'main')
      }
    }

    stage('Testing') {
      steps {
        sh 'cd app'
        sh 'python3 -m venv .venv'
        sh 'pip install -r requirements.txt'
        sh 'python3 -m unittest test_app.py'
      }
    }

  }
}