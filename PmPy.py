
from cryptography.fernet import Fernet, InvalidToken
#Vars:
masterdict = {}
x = 0

KEY_PATH = "PasswordManager.key"
# loads a key or generates a new one if a key is not found

try:
    with open(KEY_PATH, "rb") as f:
        key = f.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)

f = Fernet(key)

#======================================#


while True:
    x = x + 1 
    NewItemName = input("New Login Username: ")
    NewItemPasswrd = input("New Login Password: ")
    Profile = NewItemName
    PF_Password = NewItemPasswrd
    token = f.encrypt(PF_Password.encode('utf-8'))
    PF_Password = token
    
    tempdict = {f"{x}{Profile}" : PF_Password}
    
    TEMP = tempdict.keys() , tempdict.get("1Hello")
    print(TEMP)