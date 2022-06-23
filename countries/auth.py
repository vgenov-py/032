from os import getcwd
import json
from uuid import uuid4
from hashlib import sha1

CWD = getcwd()
file_path = f"{CWD}/users.json"

def read(file_path):
    file = open(file_path, encoding="utf8")
    data = json.load(file)
    file.close()
    return data

def write(file_path, data):
    file = open(file_path, mode="w")
    json.dump(data, file, indent=4, ensure_ascii=False)
    return True

def create_user(name, pwd):
    users = read(file_path)
    pwd = sha1(pwd.encode()).hexdigest()
    user = {
        "id": uuid4().hex,
        "name": name,
        "pwd":pwd
    }
    users["data"].append(user)
    write(file_path, users)

if __name__ == "__main__":
    # TESTING:
    create_user("test_2", "1234")
