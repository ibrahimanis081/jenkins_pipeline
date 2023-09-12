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
        dir(path: './app')
        sh 'pip install requirements.txt && python3 -m unittest test_app.py'
      }
    }

    stage('Test') {
      steps {
        sh 'cd app'
        sh 'python3 /var/lib/jenkins/workspace/jenkins_pipeline_main/app/test_app.py'
        dir(path: './app')
      }
    }

  }
}