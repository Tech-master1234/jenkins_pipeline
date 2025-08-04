node {
    stage('Preparation') {
        // Clone the GitHub repository
        git branch: 'main', url: 'https://github.com/Tech-master1234/jenkins_pipeline.git'

    }

    stage('Install Dependencies') {
        sh '''
            pip install --upgrade pip
            pip install pytest
        '''
    }

    stage('Run Tests') {
        sh '''
            pytest --junitxml=report.xml
        '''
    }

    stage('Publish Results') {
        junit 'report.xml'
    }
}