# Running Kubernetes Locally via Minikube

## Start minikube

```sh
sudo minikube start
```

> Maybe there is need to specify VM driver

```sh
sudo minikube start --vm-driver=none
```

Supported drivers:
- none (to run minikube over host with docker)
- virtualbox
- vmwarefusion
- kvm2
- kvm
- hyperkit

## Check installation

```
kubectl cluster-info
```

## Run test application exposing the service

```sh
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 --port=8080
kubectl expose deployment hello-minikube --type=NodePort
```

## Get pods


```
kubectl get pod
```
> Wait until pod is ready

```
NAME                              READY     STATUS    RESTARTS   AGE
hello-minikube-3383150820-vctvh   1/1       Running   0          13s
```

Now is possible to curl the service

```sh
curl $(minikube service hello-minikube --url)
```

## Reusing the Docker daemon (optional)

When using a single VM of Kubernetes, it’s really handy to reuse the Minikube’s built-in Docker daemon; as this means you don’t have to build a docker registry on your host machine and push the image into it - you can just build inside the same docker daemon as minikube which speeds up local experiments. Just make sure you tag your Docker image with something other than 'latest' and use that tag while you pull the image. Otherwise, if you do not specify version of your image, it will be assumed as `:latest`, with pull image policy of `Always` correspondingly, which may eventually result in `ErrImagePull` as you may not have any versions of your Docker image out there in the default docker registry (usually DockerHub) yet.

To be able to work with the docker daemon on your mac/linux host use the `docker-env` command in your shell:

```bash
eval $(minikube docker-env)
```

You should now be able to use docker on the command line on your host mac/linux machine talking to the docker daemon inside the minikube VM:

```bash
docker ps
```

Remember to turn off the imagePullPolicy:Always, otherwise Kubernetes won’t use images you built locally.

[Reference](https://kubernetes.io/docs/setup/minikube/#minikube-features)

---

# What's next
[Test kafka](https://gitlab.com/agilhernan/tfm/blob/master/doc/running_kafka.md)