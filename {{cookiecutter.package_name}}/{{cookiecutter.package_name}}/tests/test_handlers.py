import json


async def test_get(jp_fetch):
    response = await jp_fetch(
        "{{ cookiecutter.package_name | replace('-', '_') }}",
        "get_example"
    )

    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /{{ cookiecutter.package_name | replace('-', '_') }}/get_example endpoint!"
    }
