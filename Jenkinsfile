pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ibrahimanis081/jenkins_pipeline.git', branch: 'main')
      }
    }

    stage('Install') {
      steps {
        sh 'cd app && ls -la && pwd'
        sh 'ls -la && pwd'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        sh 'cd app'
        sh 'python3 test_app.py'
      }
    }

  }
}