## Installation on minikube

### Prerequisites 
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### Installation

1) Start minikube (change 192.168.49.0 if your network setup is different):
```sh
    minikube start --insecure-registry "192.168.49.0/24" --memory 12288 --cpus 4
```

2) Add Digitalhub repository:
```sh
helm repo add digitalhub https://scc-digitalhub.github.io/digitalhub/
```

3) Get minikube external IP:
```sh
    minikube ip
```

4) Install DigitalHub with Helm.

Replace the two placeholders called `MINIKUBE_IP_ADDRESS` in the command below with the output of the previous command, `minikube ip`
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --set global.registry.url="MINIKUBE_IP_ADDRESS" --set global.externalHostAddress="MINIKUBE_IP_ADDRESS" --timeout 15m0s
```

5) Wait until all pods are in Running or Completed state
```sh
kubectl --namespace digitalhub get pods
```

Once installed, you should see the references (URLs) for the different tools of the platform.

## Install with MS Azure

Documentation in progress...
