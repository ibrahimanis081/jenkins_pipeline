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
        sh 'python3 -m unittest app/test_app.py'
      }
    }

  }
}