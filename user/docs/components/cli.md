# CLI

A command-line interface (CLI) is available, allowing access to selected functionalities of the platform remotely. The CLI (`dhcli`) supports registering and switching between environments, authenticating via OAuth2 PKCE or personal access token, and managing platform resources — including projects, artifacts, models, and runs — through commands for creating, listing, retrieving, updating, and deleting them. 

It also provides utilities for uploading and downloading resources from S3, streaming run logs and metrics, accessing deployed services via local port-forwarding or an authenticated browser session, exporting environment configuration and credentials to `.env` files (`dhcli init --env`), and bootstrapping version-pinned AI agent workspaces (`dhcli init --agent`).

In-detail descriptions of the usage can be found in [this dedicated section](../cli/usage.md), and instructions for setting up AI coding assistants can be found in [Working with Agents](../tasks/agents.md).

