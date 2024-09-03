# Core

To enable the authentication with a provider for Core, you will need to set the values in the file Values.yaml of the chart digitalhub in the Core section.

The example below shows only the values concerning the authentication configuration.

```yaml
core:
  authentication:
    openId:
      enabled: true
      issuerUri: "https://yourproviderurl" # Set the issuer url of your provider
      jwtAudience: "" # Set the audience
      jwtClaim: "" # Set the claims
      oidcClientId: "" # Use this if you want to hardcode your clientID
      scope: "" # Specify the scopes
      externalSecret: # Use this if you want to get the clientID by secret.
        name: "" # Name of the secret
        key: "" # Key of the secret containing the clientID
```

In your provider, the redirect url should correspond to `https://yourcoreurl/console/auth-callback`.
