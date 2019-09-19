
import parameters
import requests
import time
import json
import time
from requests import RequestException
from json import JSONDecodeError


def option_select(count):
    options_count = list(range(1, count))
    options_count = list(map(str, options_count))
    selection = input('Selection: ')
    print("")
    while selection not in options_count:
        print('Selection Invalid')
        selection = input('Selection: ')
    return selection


def make_header():
    print("""
  1. Add keys and values manually
  2. Load header from file
  3. Go back
  
  WARNING! Loading header from a file will overwrite any keys added manually!
    """)
    selection = option_select(3)
    if selection == "1":
        key = input("Enter key: ")
        val = input("Enter value ")
        parameters.header[key] = val
        return main_menu()
    elif selection == "2":
        try:
            f = open('header.json', 'r')
            parameters.header = json.load(f)
            return main_menu()
        except JSONDecodeError:
            print("\n ERROR! Check if file is empty! \n")
            main_menu()
    elif selection == "3":
        return main_menu()


def make_body():
    try:
        print("Loading content from body.json")
        f = open('body.json', 'r')
        parameters.body = json.load(f)
        return main_menu()
    except JSONDecodeError:
        print("\n ERROR! Check if file is empty! \n")
        main_menu()


def make_payload():
    key = input("Enter key: ")
    val = input("Enter value ")
    parameters.payload[key] = val
    return main_menu()


def select_method():
    print("""
  1. Set method to GET
  2. Set method to POST
  3. Set method to OPTIONS
  4. Set method to DELETE
  """)
    menu_selection = option_select(5)
    if menu_selection == "1":
        call_type(1)
        return main_menu()
    elif menu_selection == "2":
        call_type(2)
        return main_menu()
    elif menu_selection == "3":
        call_type(3)
        return main_menu()
    elif menu_selection == "4":
        call_type(4)
        return main_menu()


def call_type(call_method):
    if call_method == 1:
        parameters.call_type = requests.get
        parameters.type_name = "GET"
    elif call_method == 2:
        parameters.call_type = requests.post
        parameters.type_name = "POST"
    elif call_method == 3:
        parameters.call_type = requests.options
        parameters.type_name = "OPTIONS"
    elif call_method == 4:
        parameters.call_type = requests.delete
        parameters.type_name = "DELETE"


def request():
    try:
        response = parameters.call_type(
            url=parameters.url,
            headers=parameters.header,
            json=parameters.body,
            params=parameters.payload
        )
        if response.ok:
            print("Response code:", response.status_code, "Call successful \n")
            parameters.response_content = response.json()
            parameters.response_header["headers"] = response.headers
            time.sleep(1)
            return main_menu()
        else:
            print("\n FAILED! \n")
            print(response.content)
            return main_menu()
    except requests.exceptions.MissingSchema as schema_error:
        print(schema_error)
        main_menu()
    except RequestException as generic_error:
        print("\n", generic_error, "\n")
        main_menu()


def result_logger():
    filename = input("Enter file name: ")
    try:
        file = open("{}.json".format(filename), "w")
        output = parameters.response_content
        json.dump(output, file, indent=4, ensure_ascii=False)
        file.close()
        print("\n File saved! \n")
        return main_menu()
    except TypeError as error:
        print(error)
        main_menu()


def main_menu():
    print("Current call method:", parameters.type_name)
    print("URL:", parameters.url)
    print("Header:", parameters.header)
    print("Body:", parameters.body)
    print("Payload:", parameters.payload)
    print("""
  1. Set call method
  2. Add URL
  3. Add header
  4. Add a JSON body
  5. Add payload
  6. Make call
  7. Print response from last call
  8. Save response to file
  9. Exit
  """)
    menu_selection = option_select(11)
    if menu_selection == "1":
        select_method()
    elif menu_selection == "2":
        url = input("Enter url: ")
        parameters.url = parameters.url_prefix + url
        return main_menu()
    elif menu_selection == "3":
        make_header()
    elif menu_selection == "4":
        make_body()
    elif menu_selection == "5":
        make_payload()
    elif menu_selection == "6":
        request()
    elif menu_selection == "7":
        print("Response body content:")
        dump = json.dumps(parameters.response_content, indent=4, ensure_ascii=False)
        print(dump, "\n")
        print("Response header:")
        print(parameters.response_header, "\n")
        return main_menu()
    elif menu_selection == "8":
        result_logger()
    elif menu_selection == "9":
        print("Exiting...")
        time.sleep(3)
        quit()
    elif menu_selection == "10":
        request()
    else:
        main_menu()


print(parameters.logo, "\n")
call_type(1)
main_menu()
