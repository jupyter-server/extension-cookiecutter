import pytest


@pytest.fixture
def jp_server_config(jp_template_dir):
    return {
        "ServerApp": {"jpserver_extensions": {"{{cookiecutter.package_name}}": True}},
    }



async def test_handler_default(jp_fetch):
    ...
