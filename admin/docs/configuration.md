# Platform Configuration

The DigitalHub Platform provides configuration options in the [DigitalHub values.yaml file](https://github.com/scc-digitalhub/digitalhub/blob/main/charts/digitalhub/values.yaml).

The safest way to set up your custom values is to use a values file in which you will set up the options you are interested in.

Thanks to the Helm hereditary properties, the platform values will change taking the values of your custom file, preserving the integrity of the originals and allowing you to use a shorter set of customized values.

You can use a custom set of values from a file like the example below, in which we install digitalhub with custom values:
```sh
helm upgrade -n <YOUR_NAMESPACE> <YOUR_RELEASE> digitalhub/digitalhub --install --create-namespace --timeout 45m0s --values <YOUR_VALUES_FILE_PATH>
```
In this example, `--set global.registry.url="MINIKUBE_IP_ADDRESS"` and `--set global.externalHostAddress="MINIKUBE_IP_ADDRESS"` are not specified in the installation command, but they can be specified in your values file:

```yaml
global:
  registry:
    url: "YOUR_ADDRESS"
  externalHostAddress: &globalExternalUrl "YOUR_ADDRESS"
```
