# Django Food Delivery – DevOps & GitOps

A Django-based food delivery application containerized with Docker, deployed on Kubernetes using Helm, automated with GitHub Actions, and managed using Argo CD GitOps.

---

## 📌 Project Overview

This project demonstrates the complete deployment lifecycle of a Django web application using modern DevOps and GitOps practices.

The application is containerized using Docker and deployed to a Kubernetes cluster running on Minikube. Helm is used to package and manage Kubernetes resources, while GitHub Actions automates the CI/CD pipeline. Argo CD continuously monitors the Git repository and synchronizes the desired state with the Kubernetes cluster.

---

## 🏗️ Architecture

```text
Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +--> Test (Django + PostgreSQL service)
    |
    +--> Docker Build & Push ------------> Docker Hub
    |
    +--> Update Helm values.yaml
              |
              v
           GitHub
              |
              v
           Argo CD
              |
              v
             Helm
              |
              v
         Kubernetes
    +---------+---------+
    |                   |
    v                   v
 Django             PostgreSQL
 Deployment         StatefulSet
    |                   |
    v                   v
 Service               PVC
    |
    v
 Ingress
    |
    v
 Browser
```

---

## 🛠️ Technologies Used

### Application
- Python
- Django
- PostgreSQL
- HTML
- CSS
- Bootstrap

### Containerization
- Docker
- Docker Hub

### Kubernetes
- Kubernetes
- Minikube
- NGINX Ingress Controller
- Deployment
- StatefulSet
- Service
- ConfigMap
- Secret
- PersistentVolumeClaim
- ServiceAccount

### DevOps & GitOps
- Git
- GitHub
- GitHub Actions
- Helm
- Argo CD

---

## 📂 Project Structure

```text
.
├── FoodManagement/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── Foods/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── food-management/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── ingress.yaml
│       ├── serviceaccount.yaml
│       ├── media-pvc.yaml
│       ├── postgres-statefulset.yaml
│       ├── postgres-service.yaml
│       ├── postgres-configmap.yaml
│       └── ...
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🔄 CI/CD Pipeline

The project uses GitHub Actions to automate the application build and deployment workflow.

When code is pushed to the `main` branch:

1. GitHub Actions checks out the source code.
2. PostgreSQL is started as a service for testing.
3. Django configuration is validated.
4. Database migrations are checked.
5. Django tests are executed.
6. A Docker image is built.
7. The Docker image is tagged using the Git commit SHA.
8. The image is pushed to Docker Hub.
9. The Helm `values.yaml` file is updated with the new image tag.
10. The updated Helm configuration is committed back to GitHub.
11. Argo CD detects the Git change.
12. Argo CD synchronizes the Helm chart with Kubernetes.
13. Kubernetes performs a rolling update using the new Docker image.

---

## 🐳 Docker

The Django application is containerized using Docker.

**Build the Docker image**

```bash
docker build -t ashish453/food--management:<tag> .
```

**Push the image**

```bash
docker push ashish453/food--management:<tag>
```

The project uses unique Git commit SHA values as Docker image tags.

Example:

```text
ashish453/food--management:cf66dfb
```

This allows different application versions to be identified and provides an easy rollback mechanism.

---

## ☸️ Kubernetes

The application is deployed to Kubernetes using Minikube.

The Kubernetes deployment contains:

- Django Deployment
- Django Service
- PostgreSQL StatefulSet
- PostgreSQL Service
- ConfigMap
- Secret
- PersistentVolumeClaim
- NGINX Ingress
- ServiceAccount

**Start Minikube**

```bash
minikube start --driver=docker
```

**Check the cluster**

```bash
kubectl get nodes
```

**Check application Pods**

```bash
kubectl get pods -n food-management-helm
```

**Check Services**

```bash
kubectl get svc -n food-management-helm
```

**Check Ingress**

```bash
kubectl get ingress -n food-management-helm
```

---

## ⎈ Helm

Helm is used to package and manage the Kubernetes resources.

The Helm chart is located at:

```text
food-management/
```

**Install or upgrade the application manually**

```bash
helm upgrade --install food-management ./food-management -n food-management-helm
```

In the GitOps workflow, however, Argo CD manages the Helm deployment.

---

## 🔁 GitOps with Argo CD

Argo CD is used to continuously synchronize the Kubernetes cluster with the desired configuration stored in Git.

The Git repository contains:

- Kubernetes/Helm configuration
- Application configuration
- Docker image tag

Argo CD monitors the repository and automatically synchronizes changes to Kubernetes.

### Argo CD Features Used

- Automatic Sync
- Automatic Pruning
- Self-Healing

### GitOps Workflow

```text
Code Change
     |
     v
Git Push
     |
     v
GitHub Actions
     |
     v
Docker Image
     |
     v
Helm values.yaml updated
     |
     v
Git Repository
     |
     v
Argo CD detects change
     |
     v
Kubernetes synchronization
     |
     v
New Application Pod
```

---

## 🌐 Accessing the Application

Start Minikube:

```bash
minikube start --driver=docker
```

Check the application:

```bash
kubectl get pods -n food-management-helm
```

Get the Minikube IP:

```bash
minikube ip
```

Check the NGINX Ingress service:

```bash
kubectl get svc -n ingress-nginx
```

The application can then be accessed through the NGINX Ingress NodePort.

Example:

```text
http://<MINIKUBE-IP>:<NODEPORT>
```

---

## 🔐 Configuration & Security

- Sensitive database credentials are stored using Kubernetes Secrets.
- Application configuration is managed using Kubernetes ConfigMaps and environment variables.
- Sensitive files such as `.env` and Kubernetes secret manifests containing real credentials are excluded from Git using `.gitignore`.

---

## 📦 Persistent Storage

PostgreSQL uses a Kubernetes PersistentVolumeClaim to persist database data.

The Django application also uses persistent storage for uploaded media files.

This allows application Pods to be recreated without automatically losing persistent data.

---

## 🔄 Deployment Strategy

The Kubernetes Deployment uses rolling updates when a new Docker image is deployed.

```text
Old Pod
  |
  | New image detected
  v
New ReplicaSet
  |
  v
New Pod
  |
  v
Old Pod terminated
```

Docker images are tagged using Git commit SHAs so each deployment corresponds to a specific version of the source code.

---

## 📊 Monitoring

Monitoring with Prometheus and Grafana is planned as a future enhancement.

Future monitoring capabilities may include:

- Kubernetes cluster metrics
- Pod CPU and memory usage
- Application request metrics
- Grafana dashboards
- Alerting with Alertmanager

---

## 🚀 Future Improvements

- Prometheus monitoring
- Grafana dashboards
- Alertmanager
- Application-level metrics
- Container security scanning
- Automated vulnerability scanning
- Cloud Kubernetes deployment
- Production-grade managed PostgreSQL

---

## 🎯 Key DevOps Concepts Demonstrated

This project demonstrates practical experience with:

- Containerization
- Docker image management
- CI/CD
- GitHub Actions
- Kubernetes
- Kubernetes networking
- Persistent storage
- Secrets and ConfigMaps
- Helm
- GitOps
- Argo CD
- Automated deployments
- Rolling updates
- Self-healing
- Infrastructure configuration through Git

---

## 👨‍💻 Author

**Ashish S N**
Computer Science & Engineering

---

## ⭐ Project Summary

A complete Django application deployment pipeline:

```text
Django
   ↓
Docker
   ↓
Docker Hub
   ↓
GitHub Actions
   ↓
Helm
   ↓
Argo CD
   ↓
Kubernetes
   ↓
NGINX Ingress
   ↓
Application
```