import pytest

pytest_plugins = ["jupyter_server.pytest_plugin"]

@pytest.fixture
def jp_server_config(jp_server_config):
     return {"ServerApp": {"jpserver_extensions": {"{{ cookiecutter.package_name | replace('-', '_') }}": True}}}
