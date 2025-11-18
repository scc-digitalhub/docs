# Create PostgREST service

We will go back to KRM to create a PostgREST service and expose the database's table via API.

## Creating the PostgREST service
Click **PostgREST Data Services** on the left and then *Create*.

Fill the first few fields as follows:

- `Name`: Anything you'd like, for example `my-postgrest`, as it's once again an identifier for Kubernetes.
- `Schema`: `public`
- Toggle on `With existing DB user`.
- `Existing DB user name`: Value of *ROLE* in the owner's secret.

Under *Connection*, fill the fields as follows:

- Toggle on `With existing secret`.
- `Secret name`: *Name* of the owner's secret.

When you hit *Save*, the PostgREST instance will be launched.

![Create PostgREST](../../images/postgrest-scenario/create-postgrest.png)

