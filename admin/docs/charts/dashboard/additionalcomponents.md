# Adding components to the Dashboard

By default, the Oltre's Dashboard displays the main components available.

If you have applications deployed in your environment that you want to show to your users, you can do so by setting the following values under the dashboard section:

```yaml
dashboard:
  #  dashboard.additional-components -- Additional components that you wish to add to your Dashboard
  additional-components:
    #  dashboard.additional-components.enabled -- Enable/Disable additional components for the Dashboard
    enabled: true
    #  dashboard.additional-components.apps -- Components to add in list format
    apps:
      - description: "Custom component description"
        existingSecret:
          #  dashboard.additional-components.apps.existingSecret.clientId -- Key of the application's clientID
          clientId: "CLIENT_ID_KEY"
          #  dashboard.additional-components.apps.existingSecret.name -- Secret containing the application's clientID and clientSecret for authentication
          name: "SECRET_NAME"
          #  dashboard.additional-components.apps.existingSecret.secretKey -- Key of the application's clientSecret
          secretKey: "SECRET_KEY_KEY"
        ingress:
          #  dashboard.additional-components.apps.ingress.enabled -- Enables Ingress.
          enabled: false
          #  dashboard.additional-components.apps.ingress.annotations -- Ingress annotations (values are templated).
          annotations: {}
          #  dashboard.additional-components.apps.ingress.hosts --
          hosts: []
          #  dashboard.additional-components.apps.ingress.ingressClassName -- Ingress Class Name. MAY be required for Kubernetes versions >= 1.18-
          ingressClassName: ""
          #  dashboard.additional-components.apps.ingress.path --
          path: /
          #  dashboard.additional-components.apps.ingress.tls -- Ingress TLS configuration.
          tls: []
        name: "Component name"
        oidcIssuerUrl: "ISSUER_URL"
        redirectUrl: "REDIRECT_URL"
        service:
          #  dashboard.additional-components.apps.service.name -- Application's service name
          name: "SERVICE_NAME"
          #  dashboard.additional-components.apps.service.port -- Application's service port
          port: "SERVICE_PORT"
```

Being a list, you can add as many apps as you want under `dashboard.additional-components.apps`.
