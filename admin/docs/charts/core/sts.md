# STS

**WARNING: this feature cannot be used locally as it depends on an Authentication Provider that should be installed in your environment.**

STS allows you to work with temporary credentials to do operations with Core to the Postgres database and the Minio bucket, avoiding the use of persistent ones and reducing the risk of a security breach.

To activate STS, set `core.sts.enabled` to `true`.
The values to activate Postgres and Minio credentials are, respectively, `core.sts.db.enabled` (set to `true` if activated) and `core.sts.minio.enabled` (set to `true` if activated).

### Credentials duration

You can set the duration of the temporary credentials in two ways.

- Setting `core.sts.credentials.duration` to the time (in seconds) you desire will set the same time for the Postgres and Minio ones
- If you wish to set them case by case, leave `core.sts.credentials.duration` as an empty string and set the time of `core.sts.credentials.minio.duration` and `core.sts.credentials.db.duration`

**NOTICE: currently, the time limit cannot be major than 28800.**
