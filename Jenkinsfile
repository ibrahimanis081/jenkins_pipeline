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
        sh 'cd app && ls -la'
        sh 'cd app && python3 -m venv .venv'
        sh 'cd app && source .venv/bin/activate'
        sh 'cd app && pip install -r requirements.txt'
        sh 'cd app && python3 -m unittest test_app.py'
        
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