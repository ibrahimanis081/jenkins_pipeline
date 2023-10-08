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
        sh 'cd app'
        sh 'ls -la'
        sh 'python3 -m venv .venv --without-pip --system-site-packages && . /var/lib/jenkins/workspace/jenkins_pipeline_main/app/.venv/bin/activate'
        sh 'pip install -r requirements.txt'
        sh 'python3 -m unittest test_app.py'
        
      }
    }
  }
}

//     stage('Build Image') {
//       steps {
//         dir(path: 'app') {
//           sh 'docker build -t ibrahimanis081/flaskapp .'
//         }

//       }
//     }

//     stage('Push') {
//       steps {
//         sh 'docker login -u "${env.DOCKERHUB_USER}" -p "${env.DOCKERHUB_PASSWORD}"'
//         sh 'docker push ibrahimanis081/flaskapp'
//       }
//     }

//   }
//   environment {
//     DOCKERHUB_USER = '____________'
//     DOCKERHUB_PASSWORD = '___________'
//   }
// }