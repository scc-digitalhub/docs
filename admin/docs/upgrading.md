# Upgrading DigitalHub

## Upgrade notes for release 0.14

**Change of definition for Core runs**

The definition for Core runs in the database has changed, so it becomes necessary to finish or stop all the current runs before upgrading to the new version.

**Change of format for Core secrets**

Core no longer accepts secrets created with a double `-` in it's name.

If you have an ongoing project that still needs your secrets, recreate them with the correct syntax.

For example, `proj-secrets--test` must become `proj-secrets--test`.

## Upgrade procedure

Once the platform is installed, you may find yourself in need of tweaking it and upgrading it.

With the command `helm upgrade` you will be able to change the values of the platform with your custom ones like the example below:

```sh
helm upgrade -n <NAMESPACE> <RELEASE> digitalhub/digitalhub --timeout 30m0s --values <YOUR_VALUES_FILE_PATH>
```

**Upgrading Coder templates**

If you wish to upgrade the Coder templates, you can do so.

You can find them in `digitalhub/charts/digitalhub/confs/coder`.

However, it is mandatory to create and set your Coder access token in the values file.

```yaml
coder:
  template:
    upgrade:
      # Set it to true if you want to upgrade the Coder templates.
      enabled: false
      # In order to upgrade the templates, you will need to create and set here a Coder Token.
      token: ""
```
