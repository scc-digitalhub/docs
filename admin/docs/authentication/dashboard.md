# Dashboard

To enable the authentication with a provider for the Dashboard, you will need to set the values in the file Values.yaml of the chart digitalhub in the Dashboard section.

The example below shows only the values concerning the authentication configuration.

```yaml
dashboard:
  oidc:
    enabled: true
    audience:
      clientId: "" # Use this if you want to hardcode your clientID
      externalSecret: # Use this if you want to get the clientID by secret.
        name: "" # Name of the secret
        key: "" # Key of the secret containing the clientID
    config:
      issuer: "https://yourproviderurl" # Set the issuer url of your provider
```
