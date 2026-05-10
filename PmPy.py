from cryptography.fernet import Fernet, InvalidToken
import json , time
#Vars:

try:
    with open("CountingX_PmPy.txt", "r") as FIleC:
    x = FileC.read()
except FileNotFoundError:
    x = 0    
masterdict = {}
tempdict = {}
y = 0 

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

# Functions:

def NewProfile(KEY=f):
    global tempdict
    global x
    x += 1
    NewItemName = input("New Login Username: ")
    NewItemPasswrd = input("New Login Password: ")
    Profile = NewItemName
    PF_Password = NewItemPasswrd
    token = KEY.encrypt(PF_Password.encode('utf-8'))
    PF_Password = token
    
    tempdict[f"{x}{Profile}"] = PF_Password
    with open("CountingX_PmPy.txt", "w") as FileC:
        FileC.write(x)
    print("New profile created.")
    return tempdict
    
def SaveNewProfile(NewPasswords):
  while True:
    userinpt = input("Are you sure you want to save? (y / n)")
    userinpt = userinpt.lower().strip()
    if userinpt in ("y", "yes"):
        print("Profile saved.")
        with open("PasswordPmPy.json", "a", encoding="utf-8") as File:
        File.write(json.dumps(new_passwords, ensure_ascii=False) + "\n")
        time.wait(2)
        break
    elif userinpt in ("n" , "no"):
        print("Aborted. (Did not save the file)")
    else:
        print("Wrong input try again")
        global y
        y += 1
        if y == 3:
            choise = input("Do you want to Abort? (y / n) ")
            if choise in ("y", "yes"):
                global y
                y = 0
                break
            elif choise in ("n" , "no"):
                global y
                y = 0
                pass


def LoadStoredProfiles():
    global masterdict
    with open("PasswordPmPy.json", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)          
            masterdict.update(obj)        


def GetProfile():
    global masterdict
    userinpt = input("Enter profile name: ")
    userinpt = userinpt.strip()
    temp = masterdict.get(userinpt)
    print(temp)
    
def DeleteProfile():
    userinpt = input().strip()
    try:
        global masterdict
        del masterdict[userinpt]
    except KeyError:
        global tempdict
        del tempdict[userinpt]
    except:
        print("Oops. Something went wrong.\n reselect this action\n by using: 'DELETE' ")
    
    
    
    
#====================================#
#Load Saved profiles
LoadStoredProfiles()
#User input
print("options are: SHOW, GET, DELETE, SAVE, NEW")
CMD = input("")
CMD = CMD.upper()

if CMD == 'NEW':
    NewProfile()
elif CMD == 'SAVE':
    SaveNewProfile(tempdict)
elif CMD == 'DELETE':
    DeleteProfile()
elif CMD == 'GET':
    GetProfile()
elif CMD == 'SHOW':
    print("Not saved profiles:")
    print(tempdict)
    print("----------------------------------")
    print("Saved profiles:")
    print (masterdict)


