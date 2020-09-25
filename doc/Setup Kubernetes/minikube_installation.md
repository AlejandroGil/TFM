# Minikube installation - single node Kubernetes cluster

## Install Docker

Add repository
```bash
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

install docker ce
> in this case, with minikube v0.30.0, docker 18.06.0
```bash
sudo apt-get update
apt-cache madison docker-ce
sudo apt-get install -y docker-ce=18.06.0~ce~3-0~ubuntu
```

test installation
```bash
sudo docker run hello-world
```

[Reference](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)

---

## Install kubectl (apt-get)

```bash
sudo apt-get update && sudo apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```
[Reference](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

---

## Install Minikube

Download the [latest release](https://github.com/kubernetes/minikube/releases) `minikube_XX.deb` file and install it

```bash
sudo dpkg -i minikube_XX.deb
```

---


# What's next

[Running Kubernetes Locally via Minikube](https://gitlab.com/agilhernan/tfm/blob/master/doc/running_minikube.md)
