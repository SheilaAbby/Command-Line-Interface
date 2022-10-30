# Python Fire is a library for automatically generating CLIs
# from absolutely any Python object.

from getpass import getpass
import fire

def login(name = None): #can pass any arg, but defaulted to "None"
    if name == None:
        name = input("What is your name \n")
    pw = getpass("What is your password\n")
    return name,pw

if __name__ == '__main__':
    fire.Fire(login)

