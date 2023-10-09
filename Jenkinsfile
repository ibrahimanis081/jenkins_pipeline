pipeline {
  agent any
  stages {

    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ibrahimanis081/jenkins_pipeline.git', branch: 'main')
      }
    }
    stage('Test Application') {
      steps {
        dir ('app') {
          sh 'python3 -m venv .venv'
          sh '. .venv/bin/activate'
          sh 'pip install -r requirements.txt'
          sh 'python3 -m unittest test_app.py'
        }
      }
    }
    stage('Build Docker Image') {
      steps {
        dir('app') {
          sh 'docker build -t ibrahimanis081/flaskapp:${BUILD_ID} .'
          }
        }
      }
    stage('Push Image To Registry') {
      steps {
        sh 'docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}'
        sh 'docker push ibrahimanis081/flaskapp:${BUILD_ID}'
      }
    }

  }
}