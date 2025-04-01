# Configuring Basic Auth for Solr

In order to use Solr with an unprivileged with Core, Solr must be configured with the basicAuth plugin (already included in the chart).

This documentation will provide an overview for the Values that you have to set and will help you finding them in the values.yaml file of the platform.

### Step 1: core.solr.collection

This section provides the necessary configuration for `core`

First, set `core.solr.collection.initialize.enabled` to true. When set to false, this value tells core to initialize everything in Solr by itself, removing the possibility of using BasicAuth. When set to true, instead, a script will initialize the Solr collection and the BasicAuth values will take effect.

Next, set `core.solr.collection.initialize.securityJsonSecret` to the name of the secret that will contain the key security.json.
Please keep in mind that the value of `core.solr.collection.initialize.securityJsonSecret` MUST be the same of `solr.solrOptions.security.bootstrapSecurityJson.name`.

### Step 2: solr.solrOptions.security

This section provides the necessary configuration for `solr`

First, choose the name for the BasicAuth secret that will be used by the operator for performing actions between Solr and your K8S environment at `solr.solrOptions.security.basicAuthSecret`.

Then, set the name of the secret containing the security.json key and corresponding data at `solr.solrOptions.security.bootstrapSecurityJson.name`.

Once again, `solr.solrOptions.security.bootstrapSecurityJson.name` value must match the one in `core.solr.collection.initialize.securityJsonSecret`. Furthermore, do not change the value of `solr.solrOptions.security.bootstrapSecurityJson.name` unless you are using an already existing secret with the required format of the Solr BasicAuth Plugin (you can set this at `solr.useExistingSecurityJson`) with a different key name.

### Step 3: solr.creds

The final step for the configuration of the BasicAuth Plugin is the configuration of the users and the credentials that will be used by Solr.

Please keep in mind that the four users (admin, k8sOper, solr, user) should be left as they are, but you should still change the passwords.

There are two values for the password configuration: `password` and `passwordSha`. The reason is that Solr requires crypted passwords in the format `sha256(sha256(salt || password))`.
While the first password will be used (as data) in the security json secret in pair with the corresponding user (as key), the corresponding encrypted password will be used directly in the security.json data as required by Solr standard.
You can either choose to encrypt it yourself or use an online tool to do it, just be sure to encrypt the correct one for every user.
