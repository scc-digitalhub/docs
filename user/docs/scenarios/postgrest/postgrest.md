# Create PostgREST service

We will go back to KRM to create a PostgREST service and expose the database's table via API.

## Inspect users' secrets

We need some parameters to configure PostgREST. Similarly to what you did in the first stage of the scenario, go to **Secrets** on the left and look for the two secrets, belonging to the *owner* and *reader* users you created.

For the **owner**, you will need the *Name* of the secret. For the **reader**, you will need the content of the *ROLE* field.

## Creating the PostgREST service
Click **PostgREST Data Services** on the left and then *Create*.

Fill the first few fields as follows:

- `Name`: Anything you'd like, it's once again an identifier for Kubernetes.
- `Schema`: `public`
- Toggle on `With existing DB user`.
- `Existing DB user name`: Value of *ROLE* in the owner's secret.

Under *Connection*, fill the fields as follows:

- `Secret name`: *Name* of the owner's secret.

When you hit *Save*, the PostgREST instance will be launched.

![Create PostgREST](../../images/postgrest-scenario/create-postgrest.png)

