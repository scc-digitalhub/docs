# Keystore

To set up a Keystore for Core, add the following section to your `values.yaml` file and configure the following fields:

```yaml
core:
  keystore:
    existingSecret:
      secretName: "keystore-secret" # Name of the secret containing the keystore
      keyName: "keystore.jwks"    # Name of the key in your keystore secret, should correspond to the keystore file name
    keystoreKid: ""  # Specify the key that the keystore should pick
    keystorePath: "/etc/keystore" # Path where your keystore will be saved
```

In this example, a Keystore will be created in the path `/etc/keystore/keystore.jwks` from a secret called `keystore-secret`.
The key of the secret, `keystore.jwks`, must contain the base64 encoded keystore.
