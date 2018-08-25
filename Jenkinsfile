node {
    def app
    
    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("julienduf/test-python:latest")
    }

    stage('Push image') {
        app.push("latest");
    }
}

