"""{{cookiecutter.project_short_description}}"""
from .extension import Extension
__version__ = "0.1.0"


def _jupyter_server_extension_points():
    return [{
        "module": "{{ cookiecutter.package_name | replace('-', '_')}}",
        "app": Extension
    }]
