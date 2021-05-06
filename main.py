import http_handler as http
import api_endpoints as API

def welcome_info():
    print(1, API.settings)
    print(2, API.login)


def print_info(method, data=""):
    if method == "GET":
        response = http.send_GET_request()
        print(response)
    elif method == "POST":
        response = http.send_POST_request(data)
        print(response)
    else:
        response = None

        
if __name__ == "__main__":
    welcome_info()
    print_info("POST", data = {
        'email': '***',
        'password': '***'
    })