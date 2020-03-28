# Create cluster

gcloud beta container clusters create mycluster \
    --enable-network-policy \
    --zone us-central1-a

# Create namespace	
kubectl create ns games

# Deploy backend api

Go inside game-api/k8s folder:

kubectl apply -f k8s.yaml

# Deploy front end app

Go inside game-app/k8s folder:

kubectl apply -f k8s.yml


# Check 1: Block all traffic from each other

kubectl apply -f 1-games-network-policy-deny-all.yaml

So now app can't access api

Reference screen shot 4


# Check 2: All traffic only between app and api

kubectl delete -f web-deny-all -n games

kubectl apply -f 2-all-policy-from-api-to-app.yaml

Check the application it works again.