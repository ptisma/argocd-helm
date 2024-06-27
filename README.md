# argocd-helm
Example fastapi app packaged in a Helm chart, used for testing the GitOps deployment on my ArgoCD instance. The Helm chart of the application is defined inside the charts folder, I was too lazy to make a separate folder for it.

## local-run
docker build -t ptisma/argocd-helm:1.0.0-main .

docker run -p 80:80 ptisma/argocd-helm:1.0.0-main
