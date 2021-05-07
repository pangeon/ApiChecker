import http_handler as http
import api_endpoints as API
from pprint import pprint  #? Show better JSON
import utils


#? package contain secret data:
import hidden.security_credentials as auth 


def welcome_info():
    print(1,"GET -->", API.settings)
    print(2,"POST -->", API.login)
    print(3,"POST -->", API.pending_payment)
    
    print('OTHER',"HTTP -->", "Enter manually URL")


def print_info(method, data=""):
    if method == "GET":
        response = http.send_GET_request()
        pprint(response)
        utils.write_to_file(response)

    elif method == "POST":
        response = http.send_POST_request(data)
        pprint(response)
        utils.write_to_file(response)
    
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
            'password': auth.password(),
            'token': None
        })
    else:
        print("Unsupported operation. Failed !")
    
    