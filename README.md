# argocd-helm
Example repo which contains two simple python based apps and their Helm charts used for testing the GitOps deployment on my ArgoCD instance. Charts are located inside the charts folder, while the good practice in GitOps is too keep them in separate repo, for the sake of simplicity I am having them in the same repo together with the rest of the code.

### apps/server
Simple fast-api server with several testing endpoints. We are injecting the env variables in two ways: static using value files and dynamic using external secrets.

Local run:
docker build -t ptisma/argocd-helm-server:1.0.0-main .

docker run -e SECRET_STR="very very secret string" -e NOT_SECRET_STR="not so secret string"  -p 80:80 ptisma/argocd-helm-server:1.0.0-main

### apps/client
Simple forever loop client which periodically tests the server's endpoint.

Local run:
docker build -t ptisma/argocd-helm-client:1.0.0-main .

docker run -e ENDPOINTS="http://host.docker.internal:80/healthz,http://host.docker.internal:80/hostname, http://host.docker.internal:80/secret, http://host.docker.internal:80/notsecret, http://host.docker.internal:80/" ptisma/argocd-helm-client:1.0.0-main

### charts
Create a chart using command helm create
In the GitOps fashion, inside the file values-main.yaml we define the values for chart which will override the default ones. This file reflects the main branch, aka the main version of this chart.

#### argocd-helm-server
Helm chart for apps/server. We defined additional resource: ExternalSecret, which will reference the ClusterSecretStore  deployed already in the cluster for fetching the actual secret key/values

