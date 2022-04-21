# {{ cookiecutter.package_name }}

[![Github Actions Status]({{ cookiecutter.repository }}/workflows/Build/badge.svg)]({{ cookiecutter.repository }}/actions/workflows/build.yml)
{%- if cookiecutter.has_binder.lower().startswith('y') -%}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{{ cookiecutter.repository|replace("https://github.com/", "") }}/main
{%- endif %}
{{ cookiecutter.project_short_description }}
{% endif %}
## Requirements

- Jupyter Server

## Install

To install the extension, execute:

```bash
pip install {{ cookiecutter.package_name }}
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall {{ cookiecutter.package_name }}
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

## Contributing

### Development install

```bash
# Clone the repo to your local environment
# Change directory to the {{ cookiecutter.package_name }} directory
# Install package in development mode - will automatically enable
# The server extension.
pip install -e .
```


You can watch the source directory and run your Jupyter Server-based application at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.  For example,
when running JupyterLab:

```bash
jupyter lab --autoreload
```

If your extension does not depend a particular frontend, you can run the
server directly:

```bash
jupyter server --autoreload
```

### Development uninstall

```bash
pip uninstall {{ cookiecutter.package_name }}
```

### Packaging the extension

See [RELEASE](RELEASE.md)
