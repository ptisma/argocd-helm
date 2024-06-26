# argocd-helm
Example fastapi app packaged in a Helm chart, used for testing on my ArgoCD instance

## local-run
docker build -t ptisma/argocd-helm:1.0.0-main .

docker run -p 80:80 ptisma/argocd-helm:1.0.0-main
