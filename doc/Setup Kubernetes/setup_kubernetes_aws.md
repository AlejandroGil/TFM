## Setup kubernetes in AWS using kops

##### Install AWS CLI
``` python
# OSX using Homebrew
brew install awscli

# Linux
pip install awscli --upgrade --user

# awscli version: 1.6.5
````

##### Install kops
```python
# OSX using Homebrew
brew install kops

# Linux
curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x kops-linux-amd64
sudo mv kops-linux-amd64 /usr/local/bin/kops

# kops version: 1.9.0
```

##### Permissions needed to deploy the cluster
```
AmazonEC2FullAccess
AmazonRoute53FullAccess
AmazonS3FullAccess
AmazonVPCFullAccess
```

##### Configure AWS CLI with the credentials
```
aws configure

AWS Access Key ID [None]: AccessKeyValue
AWS Secret Access Key [None]: SecretAccessKeyValue
Default region name [None]: eu-west-1
Default output format [None]:
```

##### Create S3 bucket for storing kops state
```bash
bucket_name=xxxxx
aws s3api create-bucket --bucket ${bucket_name} --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
```

##### Enable versioning in the bucket
```bash
aws s3api put-bucket-versioning --bucket ${bucket_name} --versioning-configuration Status=Enabled
```

##### Set K8s cluster name and set S3 URL in env variables

```bash
export KOPS_CLUSTER_NAME=xxx.k8s.local
export KOPS_STATE_STORE=s3://${bucket_name}
```

##### Define cluster
```bash
kops create cluster --help
kops create cluster --node-count=2 --node-size=t2.micro --master-size=t2.micro --zones=eu-west-1a --dns private --name=${KOPS_CLUSTER_NAME}
```

###### If any autentication issues
```bash
export AWS_ACCESS_KEY=AccessKeyValue
export AWS_SECRET_KEY=SecretAccessKeyValue
```

##### Review cluster definition
```bash
kops edit cluster --name ${KOPS_CLUSTER_NAME}
```

##### Create cluster
```bash
kops update cluster --name ${KOPS_CLUSTER_NAME} --yes
```

##### Check cluster state until it´s created
```bash
kops validate cluster
```

##### Deploy K8s dashboard
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml
```

##### Get admin password
```bash
kops get secrets kube --type secret -oplaintext
```

---

##### To power off cluster 
- See [Kops start/stop cluster](doc/kops_start_stop_cluster.md)

---

##### Deploy Kubernetes Dashboard
```bash
#get version -> https://github.com/kubernetes/dashboard 

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml
```


##### Get URL and access UI (from localhost)
```bash

kubectl proxy
http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

# --- (not necessary)
kubectl cluster-info
#set user "admin" 
https://<kubernetes-master-hostname>/ui
```

##### Get admin token to signin
```bash
kops get secrets admin --type secret -oplaintext
```
