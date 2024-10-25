pipeline {
    agent any  

    environment {
       PATH="C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
               bat "docker build -t yutika01/python Dockerfile."
            }
        }

        // stage('Docker Login') {
        //     steps {
        //         bat 'docker login -u "mca.2349@unigoa.ac.in" -p "usingforjenkins" docker.io'
        //         }
        //     }

        stage('create a container named 2349'){
          steps{
            bat "docker run --name 2349 yutika01/python"
          }
        }
      
        stage('Delete a container named 2349'){
          steps{
            bat "docker rm 2349"
          }
        }

        stage('create and run a container 2349 in daemon mode'){
          steps{
            bat "docker run -d --name 2349 yutika01/python"
          }
        }

        // stage('Push Docker Image') {
        //     steps {
        //        bat 'docker push yutika01/simage'
        //     }
        // }

        // stage('Run Docker container'){
        // steps{
        //     bat 'docker run  --name pythoncont yutika01/simage'
        // }
        // }

        // stage('Final message') {
        //     steps {
        //         echo 'Running tests...'
        //     }
        // }
        
    
    
}

    

