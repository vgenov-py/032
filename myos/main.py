import os
import datetime as dt

class MyOS:

    def __init__(self):
        pass

    @property
    def _cwd(self):
        return os.getcwd()

    def ls(self):
        return os.listdir()

    def cd(self, path):
        os.chdir(path)

    def rm(self, file):
        os.remove(file)

    def touch(self, file_name):
        file = open(file_name, "w")
        file.close()

    def mkdir(self, folder_name):
        os.mkdir(folder_name)

    def nano(self, file=""):
        os.system(f"nano {file}")
    
    def python3(self, file=""):
        os.system(f"python3 {file}")

    @staticmethod
    def date():
        return dt.datetime.now()
        
    def __str__(self):
        return self._cwd

class Ubuntu(MyOS):
    pass

def split_user(i):
    return user[i] if len(user) > i else False


if __name__ == "__main__":
    test = Ubuntu()
    user = ""
    # BASH:
    while user != "q":
        user = input(f"{test}$ ")
        user = user.split()
        command =  split_user(0)
        argument = split_user(1)

        is_command = True if command in filter(lambda method: not method.startswith("_"),dir(test)) else False

        if is_command:
            method = getattr(test, command)
            if argument:
                method(argument)
            else:
                try:
                    elements = iter(method())
                    print(*elements)
                except TypeError as e:
                    print(method())
        else:
            print(f"{command}: command not found") if command else False
    
