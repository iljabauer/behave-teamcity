pipeline {
  agent any
  stages {
    stage('Show Files') {
      steps {
        sh 'ls -lisah'
      }
    }
    stage('Build dist') {
      steps {
        sh 'python setup.py sdist bdist_wheel upload'
      }
    }
    stage('Upload') {
      steps {
        sh 'python setup.py sdist upload -r pypi'
      }
    }
  }
}