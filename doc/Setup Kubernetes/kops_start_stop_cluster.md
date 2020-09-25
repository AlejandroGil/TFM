# Stop AWS K8s cluster using kops

---

### The EC2 instances will be terminated, to start the cluster again, the process is the oposite. The cluster state will remain the same as before the stop (taking state fromm the S3 bucket) 

```bash
#scale nodes to 0 instances (min & max)
kops edit ig nodes

#get master name
kops get ig

#scale master to 0 instances
kops edit ig --name master-xxx

kops update cluster --yes
kops rolling-update cluster
```

# Start cluster

---

```bash
#scale nodes to desired instances (min & max)
export KOPS_STATE_STORE=s3://kops-state-store-agil
kops edit ig nodes

#get master name
kops get ig

#scale master to desired instances
kops edit ig master-xxx

kops update cluster --yes
kops rolling-update cluster
```