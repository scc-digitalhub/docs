# Solr

Core supports Solr integration for indexing operations.

The platform itself does not include Solr, so you will need to set it up by yourself in your environment.

Keep in mind that enabling Solr will disable Lucene automatically.

Make sure to already create the collection you want to use for Core in your instance.

### Using Solr without authentication

If you are using a Solr deployment without Basic Authentication enabled, set the following values:

```yaml
core:
  #  core.solr -- Solr configuration
  solr:
    #  core.solr.enabled -- Set this value to true if you want to use Core with an existing Solr instance
    enabled: true
    #  core.solr.collection -- Solr collection configuration
    collection:
      #  core.solr.collection.name -- Name of the Solr collection
      name: "COLLECTION_NAME"
    #  core.solr.url -- URL of your Solr instance
    url: "SOLR_INSTANCE_URL"
```

### Using Solr with Basic Auth

If you enabled authentication on your Solr instance you will still need to use the values mentioned in the previous section but you will need to set up some other things.

You have two options for the configuration:

- Specify just the admin user
- Specify both admin user and a normal user with permissions to operate on that specific collection

You will have to create a secret containing username and password for each user that you set in the values file.

The configuration for the values section can be done like this:

```yaml
core:
  #  solr -- Solr configuration
  solr:
    #  solr.enabled -- Set this value to true if you want to use Core with an existing Solr instance
    enabled: true
    #  solr.basicAuth -- Basic Auth configuration of Solr
    basicAuth:
      #  solr.basicAuth.enabled -- Set this value to true if you use BasicAuth in your Solr instance
      enabled: true
      #  solr.credentials -- Solr credentials configuration
      credentials:
        # solr.basicAuth.credentials.existingSecrets -- Existing secrets for Solr Basic Auth configuration
        existingSecrets:
          # solr.basicAuth.credentials.existingSecrets.admin -- Existing secret for Solr Basic Auth admin user
          admin:
            #  solr.basicAuth.credentials.existingSecrets.admin.passwordKey -- Password key
            passwordKey: "PASSWORD_KEY"
            #  solr.basicAuth.credentials.existingSecrets.admin.secretName -- Secret name
            secretName: "SECRET_NAME"
            #  solr.basicAuth.credentials.existingSecrets.admin.usernameKey -- Username key
            usernameKey: "USER_KEY"
          #  solr.basicAuth.credentials.existingSecrets.user -- Existing secret for Solr Basic Auth user
          user:
            #  solr.basicAuth.credentials.existingSecrets.user.passwordKey -- Password key
            passwordKey: "PASSWORD_KEY"
            #  solr.basicAuth.credentials.existingSecrets.user.secretName -- Secret name
            secretName: "SECRET_NAME"
            #  solr.basicAuth.credentials.existingSecrets.user.usernameKey -- Username key
            usernameKey: "USER_KEY"
    #  solr.collection -- Solr collection configuration
    collection:
      #  solr.collection.name -- Name of the Solr collection
      name: "COLLECTION_NAME"
    #  solr.url -- URL of your Solr instance
    url: "SOLR_INSTANCE_URL"
```
