import requests


def fixed_json_body_as_string():
    return {"Salary": "100123", "job": "QA", "Name": "Lodhi"}


def test_send_json_body_from_string_check_status_code_and_content_type():
    response = requests.post(
        "https://reqres.in/api/users",
        headers={"Content-type": "application/json"},
        json=fixed_json_body_as_string()
    )
    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

