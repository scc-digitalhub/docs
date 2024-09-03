# Ingress configuration

The services of the platform can be exposed with Ingress by editing your values file.

For every exposable component, you will find a value field for the ingress, set by default to enabled: false.

After setting enabled to true to activate the Ingress creation, check the component's values.yaml file to see how you should structure your custom values file and set all the neeeded Ingress values.

The example below is for the Core Ingress:

```yaml
ingress:
  enabled: true
  className: "youringressclass"
  hosts:
    - host: your.host
      paths: 
        - pathType: ImplementationSpecific
          path: /
  tls:
  - secretName: yourTlsSecret
```
