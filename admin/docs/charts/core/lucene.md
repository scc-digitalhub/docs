# Lucene

Lucene is the integrated and default option that Core gives you for performing indexing operations.

Lucene is included in Core without the need to configure an external component, all you have to do is set the right values to activate it.

Lucene will perform all operations in the directory specified by the value `core.lucene.indexPath` (defaults to `/lucene/`); setting this value to `false` will deactivate the tool entirely.

Persistence options will allow you to persist data in a Persistent Volume Claim created for you by the Platform chart. Keep in mind that using `ReadWriteOnce` or `ReadWriteOncePod` as Access Mode will set Core's Deployment Strategy Type to `Recreate`.

If you decide to persist your data, once the first indexing operation (during Core's application startup) is done, you can turn `core.lucene.reindex` value to `never`.

On the opposite, should you disable persistance, it is strongly reccomended to leave the option to `always`: not doing so will make you lose your Lucene data in case of a restart/crash of the Core Pod.

**WARNING: Lucene's PVC is provided by the Platform Chart; if you uninstall the release, the PVC will be destroyed, so keep that in mind.**

Below is an example of Lucene's configuration through the values.yaml file:

```yaml
core:
  lucene:
    #  core.lucene.indexPath -- Set the path for Lucene and enables it
    indexPath: "/lucene/"
    #  core.lucene.persistence -- Lucene persistence configuration
    persistence:
      #  core.lucene.persistence.enabled -- Enable persistence for Lucene
      enabled: true
      #  core.lucene.persistence.accessMode -- Access mode for the Lucene persistent volume claim
      accessMode: ReadWriteOnce
      #  core.lucene.persistence.size -- Size for the Lucene persistent volume claim
      size: 10Gi
      #  core.lucene.persistence.storageClass -- Storage class for the Lucene persistent volume claim; if not specified, the default class will be used
      storageClass: ""
    #  core.lucene.reindex -- Reindex of Lucene
    reindex: always
```
