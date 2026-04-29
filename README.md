# Streamlit Calculator CI/CD Demo

This is a simple calculator application built using Streamlit.
It is used to demonstrate Continuous Integration and Continuous Deployment
using Jenkins and GitHub.

## Features
- Addition, Subtraction, Multiplication, Division
- Automated deployment using Jenkins Pipeline
- Poll SCM trigger for CI/CD

## Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

stages:
# --- Build Stage ---
- stage: Build
  displayName: 'Build Stage'
  jobs:
  - job: BuildJob
    displayName: 'Build Job'
    steps:
    - script: |
        echo "Restoring project dependencies..."
      displayName: 'Restore dependencies'
    - script: |
        echo "Running unit tests..."
      displayName: 'Run unit tests'

# --- Test Stage ---
- stage: Test
  displayName: 'Test Stage'
  dependsOn: Build       # ensures Test runs only if Build succeeds
  condition: succeeded() # optional, explicitly enforces the rule
  jobs:
  - job: TestJob
    displayName: 'Run Tests and Publish Results'
    steps:
    - script: |
        echo "Running integration tests..."
        mkdir -p test-results
        echo "All tests passed!" > test-results/results.txt
      displayName: 'Execute Tests'
    - task: PublishTestResults@2
      inputs:
        testResultsFiles: '**/test-results/*.xml'
        testRunTitle: 'Publish Test Results'
      displayName: 'Publish Test Results to Azure DevOps'

pipeline {
    agent any

    stages {
        stage('Show Date') {
            steps {
                sh 'date'
            }
        }

        stage('Show User') {
            steps {
                sh 'whoami'
            }
        }

        stage('Show System Info') {
            steps {
                sh 'uname -a'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Loop Demo') {
            steps {
                script {
                    for (int i = 1; i <= 5; i++) {
                        echo "Iteration number: ${i}"
                    }
                }
            }
        }
    }
}


pipeline {
    agent any

    environment {
        STREAMLIT_SUPPRESS_PROMPT = 'true'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/AnushaBala1/Streamlit_Calculator_CICD.git'
            }
        }

        stage('Create Venv & Install Dependencies') {
            steps {
                bat '"C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
                bat '''
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Streamlit App') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                start "" python -m streamlit run app.py --server.headless true
                '''
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AnushaBala1/Streamlit_Calculator_CICD.git'
            }
        }

        stage('Create Virtual Environment & Install Dependencies') {
            steps {
                // Use py launcher if available, else specify full path to python
                bat """
                REM Check Python version
                py --version || echo Python launcher not found
                
                REM Create virtual environment
                py -m venv venv || "C:\\Path\\To\\Python\\python.exe" -m venv venv
                
                REM Activate venv and install requirements
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Streamlit Application') {
            steps {
                bat """
                call venv\\Scripts\\activate
                streamlit run app.py --server.port 8501 --server.headless true
                """
            }
        }
    }
}

import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number:");
        int num = sc.nextInt();

        if (num % 2 == 0) {
            System.out.println("Even number");
        } else {
            System.out.println("Odd number");
        }

        sc.close();
    }
}

import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter first number:");
        int a = sc.nextInt();

        System.out.println("Enter second number:");
        int b = sc.nextInt();

        int sum = a + b;

        System.out.println("Sum = " + sum);

        sc.close();
    }
}


#Install ansible
sudo apt update
sudo apt install ansible -y
ansible --version
ssh-keygen -t rsa
ssh-copy-id -i keyrsa ubuntuname@<ip>     #ifconfig
mkdir -p ~/ansible-setup
cd ~/ansible-setup
nano inventory.ini

[webservers]
<ip> ansible_user=ubuntuname ansible_ssh_private_key_file=~/keyrsa    #ctrl+o enter ctrl+x

ansible all -i inventory.ini -m ping
ansible-galaxy init my_web_role
cd my_web_role/tasks
nano main.yml

---
- name: Install Apache
  apt:
    name: apache2
    state: present
    update_cache: yes

- name: Ensure Apache is running
  service:
    name: apache2
    state: started
    enabled: yes

cd ..
cd..
nano site.yml

---
- name: Configure web server
  hosts: webservers
  become: true  # for using sudo

  roles:
    - my_web_role

ansible-playbook -i inventory.ini site.yml -K
cd ..
sudo systemctl status apache2
apache2 -v


cd ~/ansible-setup
nano webserver.yml

---
- name: Install Nginx Web Server
  hosts: webservers
  become: yes

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

ansible-playbook -i inventory.ini webserver.yml -K
ssh ubuntuname@<ip>
#systemctl status nginx
nginx -v
