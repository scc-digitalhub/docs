# Minio

To enable the authentication with a provider for Minio, you will need to set the values in the file Values.yaml of the chart digitalhub in the Minio section. 

The example below shows only the values concerning the authentication configuration.

```yaml
minio:
  oidc:
    enabled: true
    configUrl: "https://yourproviderurl/.well-known/openid-configuration" # Set the url of your provider
    existingClientSecretName: "" # Name of the secret containing clientID and clientSecret
    existingClientIdKey: "" # Key of the secret containing the clientID
    existingClientSecretKey: "" # Key of the secret containing the client secret
    claimName: ""  # Set the name of the JWT Claim
    scopes: "" # Set the scopes
    redirectUri: "https://yourminiourl/oauth_callback" # Set the redirect for the application
    displayName: "" # Set the name of your provider
```

Please, consult the [official Minio documentation](https://min.io/docs/minio/linux/reference/minio-server/settings/iam/openid.html#minio-server-envvar-external-identity-management-openid) for more details about the options used above.

In your provider, the redirect url should correspond to `https://yourminiourl/oauth_callback`.
