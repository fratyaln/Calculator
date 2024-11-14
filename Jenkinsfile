pipeline{
    agent any
    stages{
        stage('Clone Repository '){
            steps{
                git branch: 'main', url: 'https://github.com/fratyaln/Calculator.git'
            }
        }
        stage('Build'){
            steps{
                sh 'python3 -m py_compile Calculator.py'
            }
        }
        stage('Test'){
            steps{
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
    post {
        always{
            echo 'Cleaning up...'
        }
        success{
             echo 'Pipeline completed successfully!'
        }
        failure{
             echo 'Pipeline failed.'
        }
    }
}