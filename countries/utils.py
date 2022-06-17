import requests as req
import sys
import os
import random as rd
from typing import Union

CWD = os.getcwd()

url = "https://restcountries.com/v3.1"

if len(sys.argv) >= 2:
    WIDTH = int(sys.argv[1])
else:
    WIDTH = 50
'''
UX/UI:
'''
def clear():
    if os.name == "nt":
        os.system("cls")
        return None
    os.system("clear")
    
def center(country):
    for k,v in country.items():
            print(f"{k.upper()}: {v}".center(WIDTH))
def menu():
    print("Countries".center(WIDTH,"-"))
    print("|","1. Search contry".center(WIDTH-3), "|")
    print("|","2. Show flags".center(WIDTH-3), "|")
    print("|","3. Play country".center(WIDTH-3), "|")
    print("|","q. exit".center(WIDTH -3), "|")
    print("".center(WIDTH,"-"))

def pretty_print(country):
    for k,v in country.items():
        print(f"{k.upper()}: {v}")
'''
RESTcountries API:
'''
def get_country(country_name: str) -> dict:
    keys = ("capital", "population", "area", "languages")
    result = {k:None for k in keys}
    res = req.get(f"{url}/name/{country_name}?fullText=true")
    country = res if res.status_code == 200 else req.get(f"{url}/name/{country_name}")
    country = country.json() if country.status_code == 200 else False
    if country:
        country = country[0]
        result["capital"] = country["capital"][0]
        result["population"] = country["population"]
        result["area"] = country["area"]
        result["languages"] = tuple(country["languages"].values())
        return (result, tuple(country["flags"].values())[0])
    return False

def donwload_flag(url: str) -> bool:
    flag_name = url[-6:]
    flag_img = req.get(url)
    if flag_img.status_code == 200:
        flag_img = flag_img.content
        flag_file = open(f"{CWD}/flags/{flag_name}", "wb")
        flag_file.write(flag_img)
        flag_file.close()
        return True
    return False



if __name__ == "__main__":
    '''
    1. Acceder a la clave flag del país -> url.png | url.svg
    2. req --> url.png | url.svg --> content: bytes
    3. write file mode="wb"
    '''

    '''
    1. Listar continentes
    2 de las 5 preguntas cuantitativas, el resto características de los paises
    '''

    country, flag = get_country("spain")
    flag_img = req.get(flag).content
    flag_file = open("img.png", "wb")
    # flag_file.write(flag_img)
    flag_file.close()



    