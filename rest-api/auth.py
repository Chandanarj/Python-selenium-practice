import requests

def test_handle_auth():
    auth_data = (
        "postman", "password"
    )
    response = requests.get("https://postman-echo.com/basic-auth", auth=auth_data) 
    print(response.status_code)  
    print(response.text)
