node {
    stage('Preparation') {
        // Clone the GitHub repository
        git branch: 'main', url: 'https://github.com/Tech-master1234/jenkins_pipeline.git'

    }

    stage('Install Dependencies') {
        sh '''
            python3 -m venv venv
            source venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt || echo "No requirements.txt found"
        '''
    }

    stage('Run Tests') {
        sh '''
            . venv/bin/activate
            pytest --junitxml=report.xml
        '''
    }

    stage('Publish Results') {
        junit 'report.xml'
    }
}