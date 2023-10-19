import requests
import pytest
import json
import jsonschema
import schemas
from jsonschema import validate

BASE_URL = "https://generator.swagger.io/api"


@pytest.mark.api
def test_get_gen_clients_language_scenario():
    headers = {"accept": "application/json"}
    response = requests.get(f"{BASE_URL}/gen/clients/python", headers=headers)
    print("response: ", response.json())
    assert response.status_code == 200
    assert "urllib3" in response.json()["library"]["default"]
    schema = schemas.get_gen_clients_language_schema
    validate(instance=response.json(), schema=schema, format_checker=jsonschema.FormatChecker())


@pytest.mark.api
def test_post_gen_clients_language_scenario():
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    body = {
        "spec": {},
        "options": {
            "additionalProp1": "Test"
        },
        "swaggerUrl": "http://teststore.swagger.io/v2/swagger.json",
        "authorizationValue": {
            "value": "string",
            "type": "string",
            "keyName": "string",
            "urlMatcher": {}
        },
        "usingFlattenSpec": 'true',
        "securityDefinition": {
            "type": "string",
            "description": "string"
        }
    }

    response = requests.post(f"{BASE_URL}/gen/clients/python", headers=headers, json=body)
    print("response: ", response.json())
    assert response.status_code == 200
    assert "swagger.io" in response.json()["link"]
    schema = schemas.post_gen_clients_language_schema
    validate(instance=response.json(), schema=schema, format_checker=jsonschema.FormatChecker())

# if __name__ == "__main__":
    # to run test with python, uncomment below codes, otherwise run with pytest
    # test_gen_clients_language_scenario()
    # test_post_gen_clients_language_scenario()
    # print("All tests passed!")
