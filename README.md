## **Project Demo #1**

### **Prerequisites**

 Installed:

1. Python (3.12.8 or above)
2. Docker (latest)

### **Local**

1. Clone repository

2. `pip install -r requirements.txt `

3. Run tests with `pytest`

4. Generate and check reports with `allure serve allure_results`

### **Docker**

1. Downdload Jenkins image - ***`docker pull jenkins/jenkins`***
2. Run Jenkins image -  ***`docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins`***
3. [Install the Jenkins Allure Report plugin](https://allurereport.org/docs/integrations-jenkins/)  
4. Create a job (e.g. Allure reports)
5. Insert pipline

**Pipeline**

```
pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/ReverseBen/Project-Demo-1.git'
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the Git repository...'
                git url: env.GIT_REPO
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest tests with Allure reporting...'
                sh "pytest --alluredir=${env.ALLURE_RESULTS_DIR}"
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                sh "allure generate ${env.ALLURE_RESULTS_DIR} -o ${env.ALLURE_REPORT_DIR} --clean"
            }
        }

        stage('Publish Allure Report') {
            steps {
                echo 'Publishing Allure report...'
                allure includeProperties: false, jdk: '', results: [[path: env.ALLURE_RESULTS_DIR]]
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
            cleanWs() // Clean up the workspace
        }
    }
}
```
