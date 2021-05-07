import json
import requests

import api_endpoints as API

def select_api_enpoint():
    choice = input("Select enpoint from list above: ")
    if choice == str(1):
        return API.settings
    elif choice == str(2):
        return API.login
    elif choice == str(3):
        return API.pending_payment  
    else:
        url = input("Enter manually URL: ")
        return url 


def send_GET_request():
    try:
        url = select_api_enpoint()
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        print("MissingSchema: Please enter a valid URL")

    try:
        collection = json.loads(response.text)
        return collection
    except NameError:
        print("NameError: Please enter a valid URL")
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError: URL cannot return any data")

def send_POST_request(data):
    try:
        url = select_api_enpoint()
        response = requests.post(url, data)
    except requests.exceptions.MissingSchema:
        print("MissingSchema: Please enter a valid URL")

    try:
        collection = json.loads(response.text)
        return collection
    except NameError:
        print("NameError: Please enter a valid URL")
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError: URL cannot return any data")