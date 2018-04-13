# Simple getUser by Kucing Item Putih (12 April 2018)

from getpass import getuser

username = getuser("Username = ")
password = input("Password = ")
if (username == "admin" and password == "admin"):
    print("yay, Sucess login!")
else :
    print("wrong username / password, pls try again.")