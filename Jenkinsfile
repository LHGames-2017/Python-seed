node {
    def app
    
    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("julienduf/test-node-ts:latest")
    }

    stage('Push image') {
        app.push("latest");
    }
}
