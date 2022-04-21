from pathlib import Path

from .handlers import setup_handlers
__version__ = "0.1.0"



HERE = Path(__file__).parent.resolve()


def _jupyter_server_extension_points():
    return [{
        "module": "{{ cookiecutter.package_name }}"
    }]


def _load_jupyter_server_extension(server_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: ServerApp or ExtensionApp
        Jupyter Server application instance
    """
    setup_handlers(server_app.web_app)
    server_app.log.info("Registered {name} server extension".format(**data))


# For backward compatibility with notebook server - useful for Binder/JupyterHub
load_jupyter_server_extension = _load_jupyter_server_extension
