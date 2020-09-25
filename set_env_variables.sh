#/bin/bash
#export KOPS_STATE_STORE=s3://kops-state-store-agil
export KOPS_STATE_STORE=s3://agil2-k8s
export KOPS_CLUSTER_NAME=agil2.k8s.local
#export FISSION_ROUTER=$(kubectl --namespace fission get svc | grep router | awk '{print $4}')
