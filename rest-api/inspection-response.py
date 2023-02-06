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
    print(response.request.headers)
    print(response.request.body)
    print(response.request.url)

def test_add_user():
    json_data = {
        "name": "morpheus",
        "job": "leader"
    }   
    response = requests.post("https://reqres.in/api/users", data=json_data)
    print(response.json())
    print(response.request.body)
   