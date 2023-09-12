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
        sh 'pip install -r requirements.txt && python3 test_app.py && deactivate'
      }
    }

  }
}