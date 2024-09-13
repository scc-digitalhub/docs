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
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --set global.registry.url="MINIKUBE_IP_ADDRESS" --set global.externalHostAddress="MINIKUBE_IP_ADDRESS" --timeout 45m0s
```

5) Wait until all pods are in Running or Completed state
```sh
kubectl --namespace digitalhub get pods
```

Once installed, you should see the references (URLs) for the different tools of the platform, similar to the example below:
```
##########################################################
#   _____   _       _           _ _     _       _        #
#  (____ \ (_)     (_)_        | | |   | |     | |       #
#   _   \ \ _  ____ _| |_  ____| | |__ | |_   _| | _     #
#  | |   | | |/ _  | |  _)/ _  | |  __)| | | | | || \    #
#  | |__/ /| ( ( | | | |_( ( | | | |   | | |_| | |_) )   #
#  |_____/ |_|\_|| |_|\___)_||_|_|_|   |_|\____|____/    #
#            (_____|                                     #
#                                                        #
##########################################################

Digitalhub has been installed. Check its status by running:
  kubectl --namespace digitalhub get pods

Digitalhub componet URLs:
  - Dashboard: http://192.168.76.2:30110
  - Jupyter: http://192.168.76.2:30040 (Create jupyter workspace from template in the coder dashboard before use)
  - Dremio: http://192.168.76.2:30120 (Create dremio workspace from template in the coder dashboard before use)
  - Sqlpad: http://192.168.76.2:30140 (Create sqlpad workspace from template in the coder dashboard before use)
  - Grafana: http://192.168.76.2:30130 (Create grafana workspace from template in the coder dashboard before use)
  - Vscode: http://192.168.76.2:30190 (Create vscode workspace from template in the coder dashboard before use)
  - Docker Registry: http://192.168.76.2:30150
  - Nuclio: http://192.168.76.2:30050
  - MLRun API: http://192.168.76.2:30070
  - MLRun UI: http://192.168.76.2:30060
  - Minio API: http://192.168.76.2:30080 (Username: minio Password: minio123)
  - Minio UI: http://192.168.76.2:30090 (Username: minio Password: minio123)
  - KubeFlow: http://192.168.76.2:30100
  - Coder: http://192.168.76.2:30170 (Username: test@digitalhub.test Password: Test12456@!)
  - Core: http://192.168.76.2:30180
  - Kubernetes Resource Manager: http://192.168.76.2:30160
```

**A note for Windows, Darwin and WSL users**

As of now, due to the limitations of Minikube it is not possible to access your applications directly while using one of the OS mentioned above.

You can still access your apps from browser, but you will have to use the `kubectl port-forward` command.

For example, if you wish to expose the core service, you can use:
```sh
kubectl -n digitalhub port-forward service/digitalhub-core 30180:8080
```
This will allow you to access core by typing `localhost:30180` in your browser.

The full list of services can be checked using this command:
```sh
kubectl -n digitalhub get services
```

Please consult the official [Kubernetes documentation](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/) for more details.


## Installation on cluster

To install DigitalHub on a production environment, please consult the admin section of the documentation, where you will find informations about the configuration options and the installation as well.
