## Задание:

Задание 1:
•  Установить minikube  и запустить на нем кластер
•  Запустить на нем ingress controller
•  Установить kubectl

Задание 2:
Опубликовать приложение lesta-start:7.1 на кластере
•  подготовить deployment
•  подготовить service
•  подготовить ingress

Задание 3:
Подготовить helm chart  на основании манифестов из задания 2

## Решение:
## Задание 1
```bash
#установка docker
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER
newgrp docker

# создал новую вм для разворачивания minikube
37.9.53.206

# Установим Minikube (если еще не установлен)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# запуск кластера
minikube start --driver=docker

# установка kubectl
curl -Ls https://dl.k8s.io/release/stable.txt
VERSION=$(curl -Ls https://dl.k8s.io/release/stable.txt)
curl -LO "https://dl.k8s.io/release/${VERSION}/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client

# установка Ingress Controller
minikube addons enable ingress
kubectl get pods -n kube-system -l app.kubernetes.io/name=ingress-nginx

```
![alt text](image.png)

## Задание 2
```bash
# создание manifest
mkdir k8s-manifests
cd k8s-manifests

lesta-start-deployment.yaml
lesta-start-service.yaml
lesta-start-ingress.yaml

# применяем их в кластере с помощью kubectl
kubectl apply -f lesta-start-deployment.yaml
kubectl apply -f lesta-start-service.yaml
kubectl apply -f lesta-start-ingress.yaml

# проверка работы 
kubectl get pods
kubectl get svc
kubectl get ingress
curl http://37.9.53.82/swagger/index.html
```
![alt text](image-1.png)

## Задание 3
```bash
# Установка Helm
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list

sudo apt update
sudo apt install helm

helm version

# клонируем папку к себе на машину ./my-helm-chart
# переходим в ./my-helm-chart
helm install lesta ./lesta-start

# проверка работы 
kubectl get pods
kubectl get svc
kubectl get ingress
curl http://37.9.53.82/swagger/index.html
```

![alt text](image-2.png)

