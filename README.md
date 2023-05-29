# argo_tutorial
- minikube start
- kubectl create namespace argo
- kubectl apply -f argo {path fo yaml}
- kubectl -n argo port-forward deployment/argo-server 2746:2746
- kubectl -n argo port-forward deployment/postgres 5432:5432
- kubectl -n argo port-forward deployment/minio 9001:9001