# Core templates

You can create and use custom Core templates for your use cases.

First, create a configmap with a valid json. You can choose from the following fields:

* TO BE ADDED

The configmap should look like this:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: your-configmap
data:
  yourtemplate.json: |
    {
        "tolerations": [
            {
                "key": "nvidia.com/gpu",
                "operator": "Equal",
                "value": "a100",
                "effect": "NoSchedule"
            }
        ],
        "resources": {
            "cpu": {
                "limits": "24",
                "requests": "24"
            },
            "memory": {
                "limits": "200Gi",
                "requests": "200Gi"
            },
            "gpu": {
                "limits": "1",
                "requests": "1"
            }
        }
    }
```
Then, apply the configmap:

```sh
kubectl apply -n YOUR_NAMESPACE -f PATH_OF_YOUR_CONFIGMAP
```
Next, mount the configmap in a volume for Core by editing your values file under the Core section.

First, add the volume containing your configmap:

```yaml
core:
  volumes:
    - name: yourvolume
      configMap:
        name: yourconfigmap
```

Then, mount the volume:

```yaml
core:
  volumes:
    - name: yourvolume
      configMap:
        name: yourconfigmap  # Name of the configmap containing the template.json.
  volumeMounts:
    - name: yourvolume
      # Path in which the template will be mounted.
      # The name of the .json file must be the same as the one in the data section of your configmap.
      mountPath: test/yourtemplate.json
      subPath: yourtemplate.json
```

Finally, add the mounted template to the Core list of profiles:

```yaml
core:
  volumes:
    - name: yourvolume
      configMap:
        name: yourconfigmap
  volumeMounts:
    - name: yourvolume
      mountPath: test/yourtemplate.json
      subPath: yourtemplate.json
  profiles:
    - name: your-template-name       # Name of your template
      path: test/yourtemplate.json   # Mount path of your custom json file. Must be the same as the mountPath.
```

You can add multiple templates by following the same procedure and adding the new volume, volumeMounts and profiles to the lists.

Be sure to create a configmap for every template.

```yaml
core:
  volumes:
    - name: yourvolume
      configMap:
        name: yourconfigmap
    - name: yourvolume2
      configMap:
        name: yourconfigmap2
  volumeMounts:
    - name: yourvolume
      mountPath: test/yourtemplate.json
      subPath: yourtemplate.json
    - name: yourvolume2
      mountPath: test/yourtemplate2.json
      subPath: yourtemplate2.json
  profiles:
    - name: your-template-name
      path: test/yourtemplate.json
    - name: your-template2-name
      path: test/yourtemplate2.json
```


