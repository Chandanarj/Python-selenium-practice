import requests

def test_get_user():
    response = requests.get("https://reqres.in/api/users", 
        params={"page": "2"},
        headers={"Accept":"Application/json"}
        )
    json_data = response.json()
    #print(response.json())
    #print(response.status_code)
    #print(response.headers['Content-Type'])
    assert response.status_code == 200
    assert "application/json" in response.headers['Content-Type']
    assert json_data['page'] == 2
    assert json_data['per_page'] == 6
    assert json_data['total'] == 12
    assert json_data['total_pages'] == 2

    print(response.request.headers)
    print(response.request.body)


def test_add_user():
    json_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", data=json_data, verify=True)
    json_data = response.json()
    assert response.status_code == 201
    assert json_data['name'] == 'morpheus'
    assert json_data['job'] == 'leader'
    #print(response.json())
    print(response.request.body)

def test_update_user():
    json_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.put("https://reqres.in/api/users/2", data=json_data)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['name'] == 'morpheus'
    assert json_data['job'] == 'leader'
    #print(response.json())


def test_update_user_with_patch():
    json_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.patch("https://reqres.in/api/users/2", data=json_data)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['name'] == 'morpheus'
    assert json_data['job'] == 'leader'
    print(response.json())

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
    print(response.text)





