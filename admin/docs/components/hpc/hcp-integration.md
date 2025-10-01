# Digitalhub Platform: HCP Workload Offloading via Interlink

## Overview
Digitalhub platform leverages Kubernetes-native orchestration with the capability to dynamically offload machine learning workloads to an external HPC (High Performance Computing) cluster using the [InterLink Project](https://interlink-project.dev/docs/intro). This hybrid approach combines the flexibility of Kubernetes with the raw computational power of HPC resources for demanding ML training and inference tasks.

## Architecture
InterLink API and the plugin deployment can be arranged in three different ways across the kubernetes cluster and the remote HPC part.
Check [InterLink Project](https://interlink-project.dev/docs/intro) documentations to get more informations.

In this example we will use the **tunneled** deployment scenario.

[![InterLink Project](https://interlink-project.dev/img/scenario-3_light.svg)](https://interlink-project.dev/docs/cookbook/tunneled)

## Prerequisites
  - Kubernetes cluster (with Digitalhub platform installed)
  - Access to HCP cluster with job scheduler (Slurm, PBS, etc.)
  - Interlink project deployed and configured
  - Network connectivity between clusters
  - Appropriate authentication credentials

## Kubernetes Configuration
1. SSH Key Setup
Generate an SSH key pair if you don't have one:
```sh
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/interlink_rsa

# Copy private key to remote server
scp ~/.ssh/interlink_rsa user@remote-server:~

# Test SSH connection
ssh -i ~/.ssh/interlink_rsa user@remote-server
```

2. Interlink Setup
Deploy the Interlink on your kubernetes cluster:

```sh
helm install --create-namespace -n interlink virtual-node \
  oci://ghcr.io/intertwin-eu/interlink-helm-chart/interlink \
  --values my-values.yaml
```
my-values.yaml:
```yaml title="my-values.yaml"
nodeName: interlink-socket-node

interlink:
  enabled: true
  socket: unix:///var/run/interlink.sock

plugin:
  socket: unix:///var/run/plugin.sock

sshBastion:
  enabled: true
  clientKeys:
    authorizedKeys: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI..." # Previosly createt public key
  port: 31022

virtualNode:
  resources:
    CPUs: 8
    memGiB: 32
    pods: 100
```
## HPC Configuration
1. Download [interlink-slurm-plugin](https://github.com/interlink-hq/interlink-slurm-plugin/releases) on your login node.
2. Configure InterLink Slurm plugin to listen on a Unix socket instead of a TCP port:
```yaml
SidecarPort: ""
Socket: "unix:///var/run/plugin.sock"
SbatchPath: "/usr/bin/sbatch"
ScancelPath: "/usr/bin/scancel"
SqueuePath: "/usr/bin/squeue"
SinfoPath: "/usr/bin/sinfo"
CommandPrefix: ""
SingularityPrefix: ""
SingularityPath: "singularity"
ExportPodData: true
DataRootFolder: ".local/interlink/jobs/"
Namespace: "vk"
Tsocks: false
TsocksPath: "$WORK/tsocks-1.8beta5+ds1/libtsocks.so"
TsocksLoginNode: "login01"
BashPath: /bin/bash
VerboseLogging: true
ErrorsOnlyLogging: false
ContainerRuntime: singularity
EnrootDefaultOptions: ["--rw"]
EnrootPrefix: ""
EnrootPath: enroot
```
3. On the remote HCP login node, start your interLink plugin:
```sh
# Example: Start SLURM plugin on remote HPC system
cd /path/to/plugin
SLURMCONFIGPATH=/root/SlurmConfig.yaml SHARED_FS=true /path/to/plugin/slurm-sidecar
```

4. Forward slurm plugin Unix socket to ssh the bastion host:
```sh
ssh -nNT -L /var/run/plugin.sock:/var/run/plugin.sock user@sshbastiononkubernetes
```

## Post-Installation

### Verify Deployment

```bash
# Check virtual node status
kubectl get node <nodeName>

# Check pod status
kubectl get pods -n interlink

# View virtual node details
kubectl describe node <nodeName>

# Check logs
kubectl logs -n interlink deployment/<nodeName>-node -c vk
```

### Testing the Virtual Node

```yaml
# test-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-workload
spec:
  nodeSelector:
    kubernetes.io/hostname: <nodeName>
  containers:
  - name: test
    image: busybox
    command: ["sleep", "3600"]
```

```bash
kubectl apply -f test-pod.yaml
kubectl get pod test-workload -o wide
