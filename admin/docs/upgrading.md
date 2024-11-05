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

**Upgrading from Digitalhub 0.7 to 0.8**

This section is aimed only for environments with an already running instance of Digitalhub. 

Due to the removal of MLRun, the upgrading process needs some extra steps.

Follow this guide to upgrade your installation while keeping your existing environment stable:

1) Clone the [repository of Digitalhub](https://github.com/scc-digitalhub/digitalhub). You will need to apply some CRDS manually.

2) Apply the CRDS inside the folder `digitalhub/charts/kubeflow-pipelines/crds` in your namespace. Most of the CRDS are the same as the one applied with the MLRun chart, but some are not and are needed for the standalone installation of Kubeflow Pipelines.

3) The MLRun chart included a MySql depolyment, but, although the Kubeflow Pipelines chart uses the same approach, the MySql version used (8.0.26) is greater then the one installed with MLRun, therefore it is necessary to remove the existing MySql deployment and the associated PVC.

If your environment, instead of the embedded one, used an external deployment of MySql with a version compatible with 8.0.26, you can choose to keep it setting the values accordingly. Please, check the [MySql configuration guide for KFP](charts/kfp/mysql.md) for more details.

4) You can now upgrade to Digitalhub 0.8.0. After the installation, make sure that the crds inside `digitalhub/charts/kubeflow-pipelines/crds` have been all correctly applied.

