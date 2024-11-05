# KRM roles

[Enabling authentication for the Kubernetes Resource Manager](../../authentication/krm.md) is required to use this feature.

Setting up roles can be a great way for assigning permissions to the users of the Kubernetes Resource Manager, setting up limitations to what they can do and the resources they can have access to.

To set up your custom KRM roles and permissions, follow this example and change the fields to your needs in your Values file:

```yaml
kubernetes-resource-manager:
  oidc:
    roleClaim: "krm_roles"    # Name of the role used 
    access:
      roles:
        - role: ROLE_MY_ROLE  # Name of the role
          # Resources associated to the role with permissions
          resources: k8s_service, k8s_secret::read, mycrd/example.com::write
```

In this basic example we create a Role called ROLE_MY_ROLE that will have:

- Access to the services
- Access with read permissions to the secrets
- Access with write permissions to a custom CRD

You will also have to setup your authentication provider accordingly, so that you can associate the correct role to the correct users.
