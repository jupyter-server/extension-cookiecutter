from jupyter_server.extension.application import ExtensionApp
from .handlers import RouteHandler


class Extension(ExtensionApp):

    name = "{{ cookiecutter.package_name | replace('-', '_') }}"
    handlers = [
        ("{{ cookiecutter.package_name | replace('-', '_') }}/get_example", RouteHandler)
    ]

    # mytrait = Unicode("").tag(config=True)
