## Installation on minikube

### Prerequisites 
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### Installation

1. Start minikube (change 192.168.49.0 if your network setup is different):
```sh
    minikube start --insecure-registry "192.168.49.0/24" --memory 12288 --cpus 4
```
2. Get minikube external IP:
```sh
    minikube ip
```
3. Change the IP in  'global.registry.url' and 'global.externalHostAddress' properties in values file (*chart/digitalhub/values.yaml*) with the one obtained in the previous step. 
  
There are two main ways to do this step:
- Cloning the repo at https://github.com/scc-digitalhub/digitalhub and editing the values file. Use this method if you want to vastly customize your installation.
- Setting the specific values with the installation command, useful if you want to edit a low number of values. 
    
The two options will be covered in the installation step.  

4. Add Digitalhub repository:
```sh
helm repo add digitalhub https://scc-digitalhub.github.io/digitalhub/
```
5. Install DigitalHub with Helm:
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --timeout 15m0s
```

If you want to install Digitalhub with your values, you can do so by applying small changes to the previous command.

Install Digitalhub with your values file:
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --values PATH_TO_VALUES_FILE --timeout 15m0s
```
Install Digitalhub setting specific values:
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --set global.registry.url="MINIKUBE_IP_ADDRESS" --set global.externalHostAddress="MINIKUBE_IP_ADDRESS" --timeout 15m0s
```

6. Wait until all pods are in Running or Completed state
```sh
kubectl --namespace digitalhub get pods
```

Once installed, you should see the references (URLs) for the different tools of the platform.

7. After the installation process you can still edit the platform with the values file if you need to make some changes/adjustments.

Upgrading Digitalhub with your values file:
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --values PATH_TO_VALUES_FILE --timeout 15m0s
```
Upgrading Digitalhub setting specific values:
```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --set global.registry.url="MINIKUBE_IP_ADDRESS" --set global.externalHostAddress="MINIKUBE_IP_ADDRESS" --timeout 15m0s
```

## Install with MS Azure

Documentation in progress...
