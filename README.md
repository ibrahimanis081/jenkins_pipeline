<!-- PROJECT TITLE AND LOGO -->
<br />
<div align="center">
  
   <h3 align="center">Automated CI/CD Pipeline for Python Flask Web App</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project involves setting up a Python Flask web application with an integrated Jenkins CI pipeline. The pipeline automates code testing, image building, and image deployment to DockerHub.

Pipeline Steps:

* Push Trigger: Any push to this repository's main branch triggers the Jenkins pipeline.
* Testing: The pipeline runs unit tests on the Python Flask application to ensure code integrity and correctness.
* Building: Upon successful testing, the code is built, packaged, and prepared for deployment.
* Docker Image Creation: The application is containerized into a Docker image.
* Docker Image Push: The Docker image is pushed to DockerHub, making it accessible for deployment in various environments.
* Deployment: (to be done) The Docker image to be deployed to kubernetes through argocd.


### Built With
<br/>


* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)






