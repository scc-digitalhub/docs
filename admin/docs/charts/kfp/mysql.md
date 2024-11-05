# Database configuration

Kubeflow Pipelines uses a MySql database for data storage.
This section describes how to set it up properly taking into account two use cases.

### Use case 1: creating a new database

By default, the Kubeflow Pipelines chart creates a new MySql database with a root user and an unprivileged user.

To achieve this goal, set the values accordingly in the `kubeflow-pipelines` section of the `values.yaml` file:

```yaml
kubeflow-pipelines:
  # These values crate a new mysql deployment using rootUsername and rootPassword for the admin account.
  embeddedMySql:
    enabled: true       # Enable the creation of a new MySql database
    rootUsername: root  # Username of the root user
    rootPassword: pwd   # Password of the root user
  db:
    # Set the username and password for the unprivileged user of a new mysql database deployment.
    username: mysqluser # Username of the unprivileged user
    password: pwd       # Password of the unprivileged user
```

### Use case 2: using an already existing database

#### Prerequisites:
- An already existing MySql in your environment
- A secret containing two keys, one for the username and one for the password of the MySql user you wish to use
- Two databases named `mlpipeline` and `metadb`
- The user that you wish to use MUST have permissions to work on the above mentioned databases

In case you have an already existing MySql in the same environment that you wish to use, you can set the values like the following example:

```yaml
kubeflow-pipelines:
  embeddedMySql:
    enabled: false      # Disable the creation of a new MySql database
  db:
    # If you have an already existing mysql database that you want to use, you must provide the secret containing username and password of the user.
    # WARNING: if you want to use an existing mysql deployment, make sure to:
    # - Have two databases, "metadb" and "mlpipeline"
    # - In the secret, specify a user that has privileges on the two above mentioned databases
    externalSecret:
      secretName: "mysql-user-secret"   # Name of the secret cotaining username and password of the MySql user
      usernameKey: "username"           # Name of the key cotaining the username the MySql user
      passwordKey: "password"           # Name of the key cotaining the password of the MySql user
```
