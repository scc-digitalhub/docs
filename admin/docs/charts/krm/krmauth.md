# Enabling authentication for Kubernetes Resource Manager

To enable the authentication with a provider for Kubernetes Resource Manager, you will need to set the values in the file Values.yaml of the chart digitalhub in the Kubernetes Resource Manager section. 

The example below shows only the values concerning the authentication configuration.

```yaml
kubernetes-resource-manager:
  oidc:
    enabled: true
    audience:
      clientId: "" # Use this if you want to hardcode your clientID
      externalSecret: # Use this if you want to get the clientID by secret.
        name: "" # Name of the secret
        key: "" # Key of the secret containing the clientID
    issuer: "https://yourproviderurl" # Set the issuer url of your provider
    scope: "" # Set the scopes
    authType: "" # Set the type of authentication
```

In your provider, the redirect url should correspond to `https://yourkubernetesresourcemanagerurl/console/auth-callback`.
