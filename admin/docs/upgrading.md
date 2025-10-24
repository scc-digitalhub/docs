# Upgrading DigitalHub

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
