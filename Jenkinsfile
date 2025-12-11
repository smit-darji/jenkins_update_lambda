pipeline {
    agent any

    environment {
        AWS_CREDENTIALS = 'aws-lambda-deployer'       // Jenkins credential ID
        AWS_REGION = "ap-south-1"                    // Change if needed
        LAMBDA_FUNCTION = "jenkins-poc-lambda"       // Your Lambda name
    }

    triggers {
        githubPush()                                  // Runs when GitHub pushes to master
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/YOUR-ORG/jenkins_update_lambda.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    cd lambda_function
                    pip install -r requirements.txt -t .
                """
            }
        }

        stage('Package Lambda') {
            steps {
                sh """
                    cd lambda_function
                    zip -r ../lambda.zip .
                """
            }
        }

        stage('Update Lambda Function') {
            steps {
                withAWS(credentials: AWS_CREDENTIALS, region: AWS_REGION) {
                    awsLambdaUpdate(
                        functionName: LAMBDA_FUNCTION,
                        zipFile: "lambda.zip"
                    )
                }
            }
        }
    }

    post {
        success {
            echo "Lambda updated successfully."
        }
        failure {
            echo "Lambda update failed."
        }
    }
}
