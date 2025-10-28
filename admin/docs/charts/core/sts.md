# STS

**WARNING: this feature cannot be used locally as it depends on an Authentication Provider that should be installed in your environment.**

STS allows you to work with temporary credentials to do operations with a Postgres database, avoiding the use of persistent ones and reducing the risk of a security breach.

To activate STS, set `core.sts.enabled` to `true`.

There are a lot of values to cover, so the example will be divided in three parts.


## Setting STS clientId and clienSecret

As a first step, set ClientID and ClientSecret for STS. You can either specify them hardcoded or via secret (better choice for production environments).

```yaml
core:
  sts:
    #  sts.enabled -- Enable/Disable STS component for dynamic credentials
    enabled: false
    #  sts.client --
    client:
      #  sts.client.clientId -- ClientID used by STS
      clientId: ""
      #  sts.client.clientSecret -- ClientSecret used by STS
      clientSecret: ""
      #  sts.client.existingSecret --
      existingSecret:
        #  sts.client.existingSecret.clientIdKey -- Key corresponding to the STS ClientID
        clientIdKey: "CLIENTID"
        #  sts.client.existingSecret.clientSecretKey -- Key corresponding to the STS ClientSecret
        clientSecretKey: "CLIENTSECRET"
        #  sts.client.existingSecret.name -- Name of the secret containing STS ClientID and ClientSecret
        name: "YOUR_STS_SECRET"
```

## Configuring STS database

STS itself needs it's own database so you'll need to set the connection with it as well.

Here is an example configuration:

```yaml
core:
  sts:
    #  core.sts.stsDb -- Values of the STS database
    stsDb:
      #  core.sts.stsDb.credentials -- Credentials of the STS database
      credentials:
        #  core.sts.stsDb.credentials.existingSecret -- Reference to the secret containing username and password of the STS database user.
        #  These values have higher priority than the explicit declarations.
        existingSecret:
          #  core.sts.stsDb.credentials.existingSecret.name -- Name of the secret containing username and password of the STS database user
          name: "YOUR_STS_DB_OWNER"
          #  core.sts.stsDb.credentials.existingSecret.passwordKey -- Key corresponding to the STS database user password
          passwordKey: "OWNER_PASSWORD_KEY"
          #  core.sts.stsDb.credentials.existingSecret.usernameKey -- Key corresponding to the STS database user username
          usernameKey: "OWNER_USERNAME_KEY"
        #  core.sts.stsDb.credentials.password -- Explicit declaration of the STS database user password.
        #  It has lower priority than the corresponding secret values.
        password: ""
        #  core.sts.stsDb.credentials.username -- Explicit declaration of the STS database user username.
        #  It has lower priority than the corresponding secret values.
        username: ""
      #  core.sts.stsDb.database -- Name of the STS database
      database: "STS_DATABASE_NAME"
      #  core.sts.stsDb.driver -- Driver used by the STS database
      driver: "STS_DB_DRIVER"
      #  core.sts.stsDb.host -- Host of the STS database
      host: "STS_DATABASE_HOSTNAME"
      #  core.sts.stsDb.platform -- Which kind of database you are using for STS (For example, postgresql)
      platform: "postgresql"
      #  core.sts.stsDb.port -- STS Database port
      port: "5432"
      #  core.sts.stsDb.schema -- STS database schema
      schema: "public"
```

## Configuring the Database that will use the temporary credentials

Now that you have configured the connection with the STS database, all that's left is configuring the connection with the Platform's main database:

```yaml
core:
  sts:
    #  sts.credentials --
    credentials:
      #  sts.credentials.roles -- Roles that will be mapped to the user for Database operations.
      #  Must correspond to the owner user of the Platform's main database.
      roles: "OWNER_USER"
    #  sts.databaseProvider -- Values of the Platform's main database
    databaseProvider:
      #  sts.databaseProvider.enabled -- Enable/Disable dynamic credentials for Postgres operations.
      enabled: true
      #  sts.databaseProvider.credentials -- Credentials of the Platform's main database
      credentials:
        #  sts.databaseProvider.credentials.existingSecret -- Reference to the secret containing username and password of the Platform's main database owner user.
        #  These values have higher priority than the explicit declarations.
        existingSecret:
          #  sts.databaseProvider.credentials.existingSecret.name -- Name of the secret containing username and password of the Platform's main database owner user
          name: "OWNER_SECRET"
          #  sts.databaseProvider.credentials.existingSecret.passwordKey -- Key corresponding to the Platform's main database owner user password
          passwordKey: "OWNER_PWD"
          #  sts.databaseProvider.credentials.existingSecret.usernameKey -- Key corresponding to the Platform's main database owner user username
          usernameKey: "OWNER_USERNAME"
        #  sts.databaseProvider.credentials.password -- Explicit declaration of the Platform's main database owner user password.
        #  It has lower priority than the corresponding secret values.
        password: ""
        #  sts.databaseProvider.credentials.username -- Explicit declaration of the Platform's main database owner user username.
        #  It has lower priority than the corresponding secret values.
        username: ""
    #  sts.jwt --
    jwt:
      #  sts.jwt.issuerUri -- URL of the JWT issuer.
      issuerUri: ISSUER_URL
```
