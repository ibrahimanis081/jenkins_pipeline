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
        sh '''python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python test_app.py
deactivate

'''
      }
    }

  }
}