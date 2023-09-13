pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ibrahimanis081/jenkins_pipeline.git', branch: 'main')
      }
    }

    stage('Test App') {
      steps {
        dir(path: 'app') {
          sh 'ls -la'
          sh 'python3 -m venv .venv --without-pip --system-site-packages && . /var/lib/jenkins/workspace/jenkins_pipeline_main/app/.venv/bin/activate'
          sh 'python3 -c "import sys; print(sys.path)"'
          sh '''pip install -r requirements.txt && python3 -m unittest test_app.py
'''
        }

      }
    }

  }
}