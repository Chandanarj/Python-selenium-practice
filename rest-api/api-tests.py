import requests

def test_get_user():
    response = requests.get(
        "https://reqres.in/api/users",
         params={'page': '2'},
         headers={'Accept': 'application/json'},
        )
    print(response.json())
    print(response.status_code )
    print(response.headers['Content-Type'] )

def test_add_user():
    json_data = {
        "name": "morpheus",
        "job": "leader"
    }   
    response = requests.post("https://reqres.in/api/users", data=json_data)
    print(response.json())

def test_update_user():
    json_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put("https://reqres.in/api/users/2", data=json_data)
    print(response.json())

def test_update_user_using_patch():
    json_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch("https://reqres.in/api/users/2", data=json_data)
    print(response.json())

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    print(response.content)

def test_basic_auth():
    auth = ('postman', "111")
    response = requests.get("https://postman-echo.com/basic-auth", auth= auth)
    print(response.text)
    print(response.status_code)