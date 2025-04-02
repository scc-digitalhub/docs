# Using the platform externally

A command-line interface (CLI) is available, allowing access to certain functionalities of the platform remotely. It can be used to set up the environment and install the Python packages.

## CLI installation

Download the latest version of the CLI for your OS from its [releases page on GitHub](https://github.com/scc-digitalhub/digitalhub-cli/releases). Extract the archive and open a console in the path of the `dhcli` file.

### MacOS

On MacOS, it can be installed using Homebrew Tap:

``` sh
brew tap scc-digitalhub/digitalhub-cli https://github.com/scc-digitalhub/digitalhub-cli
brew install dhcli
```

## CLI usage

The standard use flow of the CLI is as follows:

1. Register your instance's configuration. This creates a `.dhcore.ini` file in your home directory (or, if not possible, in the current one), where the configuration will be stored, to be used and updated by subsequent commands.

``` sh
./dhcli register http://localhost:8080
```

2. Log in. This will open a tab in your Internet browser, where you will have to carry out the log in procedure.

``` sh
./dhcli login
```

3. If you wish to install the python packages, `init` will do so, matching the platform's version.

``` sh
./dhcli init
```

In-detail descriptions of available commands can be found in [this dedicated section](../components/cli_commands.md).