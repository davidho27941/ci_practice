pipeline {
	agent {
		docker {
			image 'davidho9717/ubuntu:HEPSimulation-minimal'
			args '-d -p 8000:8000'
		}
	}
	stages {
		stage('Build') {
			steps {
				sh 'python -m pip install --upgrade pip'
				sh 'python -m pip install pytest flake8'
				sh 'python -m pip install -r requirements.txt'
				sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
				sh 'flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
				sh 'pytest test.py'
			}
		}
	}
}
