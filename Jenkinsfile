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
        dir ('app') {
          sh 'ls -la'
          sh 'python3 -m venv .venv'
          sh 'ls -la'
          sh '. .venv/bin/activate'
          sh 'pip install -r requirements.txt'
          sh 'python3 -m unittest test_app.py'
          sh 'echo buildno${BUILD_ID}'
          }
        
        }
      }
    stage('Build Image') {
      steps {
        dir('app') {
          sh 'ls -la'
          sh 'docker build -t ibrahimanis081/flaskapp .'
          }
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
 // :${BUILD_ID}
//     DOCKERHUB_USER = '____________'
//     DOCKERHUB_PASSWORD = '___________'
//   }
// }