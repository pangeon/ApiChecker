# ApiChecker

Testing tools for API services.

## Secret package

1. create folder has name **hidden**
2. create **init.py** (name with underscores) and **security_credentials.py**
3. create method in **security_credentials.py**

   ```
       def email():
           return email

       def password():
           return password
   ```

## Config your code

- **api_enpoints.py** contains api URLs addresses.
- In **http_handler.py** you might add enpoints to list.

  ```
  def select_api_enpoint():
      choice = input("Select enpoint from list above: ")
      if choice == str(1):
          return API.settings
      elif choice == str(2):
          return API.login

      <-- ADD NEW ENPOINT -->

      else:
          url = input("Enter manually URL: ")
          return url
  ```

- In **main.py** config info for users:

  ```
  def welcome_info():
      print(1,"GET -->", API.settings)
      print(2,"POST -->", API.login)

      <-- ADD NEW INFO -->

      print('OTHER',"HTTP -->", "Enter manually URL")
  ```

# Author

- [Kamil Cecherz](http://cecherz.pl/)
