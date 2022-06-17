import json
import os
from utils import *
clear()
user = ""
while user != "q":
    menu()
    user = input("option: ")
    clear()
    menu()
    if user == "1":
        country_name=input("Country: ")
        clear()
        menu()
        country, flag = get_country(country_name)
        if country:
            center(country)
        else:
            "No encontramos nah"
        is_flag=input("Download flag?(Y/N): ").lower()
        if is_flag == "y":
            if donwload_flag(flag):
                print("Download successful") 
                input("...")
    elif user == "2":
        clear()
        flags = os.listdir(f"{CWD}/flags")
        for i, flag in  enumerate(flags):
            print(f"{i+1}. {flag}")
        
        user = int(input(": "))
        os.remove(f"{CWD}/flags/{flags[user-1]}")
    clear()
