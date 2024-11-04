# Devcontainer, the Gihub Codespaces configuration file

This configuration is intended for [Github Codespaces](https://docs.github.com/en/codespaces) users.

The `devcontainer.json` file allows to specify a configuration that can be used to create a Codespace.

Refer to the official [Codespaces devcontainers documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration) for more information.

## Elements

The code below forces the installation of the MDX extension for VSCode inside a Codespace.

    ```json
    {
      "customizations": {
        "vscode": {
          "extensions": ["unifiedjs.vscode-mdx"]
        }
      }
    }
    ```

**Note:** The identifier of the extension (e.g. `unifiedjs.vscode-mdx`) can be found on the VSCode extension page, under "More info".