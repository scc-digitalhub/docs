# Kubeflow

To enable the authentication with a provider for Kubeflow, you will need to set the values in the file Values.yaml of the chart digitalhub in the OAuth2 Proxy section. 

The applications using OAuth2 Proxy are specified as a list and should be added together one after the other.

The example below shows only the values concerning the authentication configuration.

```yaml
oauth2-proxy:
  enabled: true
  apps:
    - redirectUrl: "https://yourkubeflowurl/oauth2/callback" # Set the redirect url for the application
      oidcIssuerUrl: "https://yourproviderurl" # Set the url of your provider
      existingSecret:
        name: "" # Name of the secret containing clientID and clientSecret
        clientId: "clientid" # Key of the secret containing the clientID
        secretKey: "clientsecret" # Key of the secret containing the client secret
```
