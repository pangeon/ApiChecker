import http_handler as http
import api_endpoints as API


#? package contain secret data:
import hidden.security_credentials as auth 


def welcome_info():
    print(1,"GET -->", API.settings)
    print(2,"POST -->", API.login)
    
    print('OTHER',"HTTP -->", "Enter manually URL")


def print_info(method, data=""):
    if method == "GET":
        response = http.send_GET_request()

        try:
            for key, value in response.items():
                print(key + ":", value)
        except AttributeError:
            print(response)

    elif method == "POST":
        response = http.send_POST_request(data)

        try:
            for key, value in response.items():
                print(key + ":", value)
        except AttributeError:
            print(response)
    
    else:
        response = None

        
if __name__ == "__main__":
    welcome_info()
    option = str(input("Wchich method you want invoke: GET or POST: "))
    if option == 'GET':
        print_info("GET")
    elif option == 'POST':
        print_info("POST", data = {
            'email': auth.email(),
            'password': auth.password()
        })
    else:
        print("Unsupported operation. Failed !")
    
    