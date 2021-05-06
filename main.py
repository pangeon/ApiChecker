import http_handler as http
import api_endpoints as API

def welcome_info():
    print(1, API.settings)
    print(2, API.login)


def print_info(method, data=""):
    if method == "GET":
        response = http.send_GET_request()

        for key, value in response.items():
            print(key + ":", value)
    elif method == "POST":
        response = http.send_POST_request(data)

        for key, value in response.items():
            print(key + ":", value)
    else:
        response = None

        
if __name__ == "__main__":
    welcome_info()
    print_info("GET")
    # print_info("POST", data = {
    #     'email': '***',
    #     'password': '***'
    # })