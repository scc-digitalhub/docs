# Installation on cluster

### Prerequisites 
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- A configured image registry
- A configured DNS
- Domains and Ingress Controller for service exposition
- A configured OAuth provider to enable authentication

### Installation

Once you have set your custom values.yaml file, DigitalHub can be installed as follows:

1) Add Digitalhub repository:
```sh
helm repo add digitalhub https://scc-digitalhub.github.io/digitalhub/
```


2) Install DigitalHub with Helm and your custom values.

```sh
helm upgrade digitalhub digitalhub/digitalhub -n digitalhub --install --create-namespace --values PATH_TO_YOUR_VALUES_FILE --timeout 45m0s
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
  - Docker Registry: http://192.168.76.2:30150
  - Coder: http://192.168.76.2:30170 (Username: test@digitalhub.test Password: Test12456@!)
  - Core: http://192.168.76.2:30180
  - Kubernetes Resource Manager: http://192.168.76.2:30160
```  
