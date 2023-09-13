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
        dir(path: 'app') {
          sh 'ls -la'
          sh '''pip install -r requirements.txt && python3 -m unittest test_app.py
'''
        }

      }
    }

  }
}