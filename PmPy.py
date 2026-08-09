from cryptography.fernet import Fernet, InvalidToken
import json , time
#Vars:

masterdict = {}
tempdict = {}
y = 0

Flag = True 

                      
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

#print(f) # debug


#======================================#

# Functions:

def NewProfile(KEY=f):
    global tempdict
    NewItemName = input("New Login Username: ")
    NewItemPasswrd = input("New Login Password: ")
    Profile = NewItemName
    PF_Password = NewItemPasswrd
    token = KEY.encrypt(PF_Password.encode('utf-8'))
    PF_Password = token
    tempdict[NewItemName] = token.decode("utf-8")
    print("New profile created.")
    

def SaveNewProfile():
    global tempdict
    userinpt = input("Are you sure you want to save? (y / n) ").lower().strip()
    if userinpt in ("y", "yes"):
        with open("PasswordPmPy.json", "w", encoding="utf-8") as File:
            json.dump(tempdict, File)
        print("Profile saved.")


def LoadStoredProfiles():
    global masterdict
    try:
        with open("PasswordPmPy.json", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                masterdict = obj
    except FileNotFoundError:
        with open("PasswordPmPy.json", "w", encoding="utf-8") as f:
            f.close()


def GetProfile():
    global masterdict
    global tempdict
    global f
    userinpt = input("Enter profile name: ").strip()
    print("--------------------------------")
    if userinpt in tempdict:
        print(f"There is a profiled named {userinpt} that isn't saved.")
        DecryptedPass = f.decrypt(tempdict[userinpt].encode("utf-8"))
        print(DecryptedPass)
    else:
        print(f"There isn't a not-saved profile named {userinpt}:")
    print("----------------------------------------")
    EncryptedPass = masterdict.get(userinpt)
    if EncryptedPass == None:
        print(f"There isn't a saved profile named {userinpt}:")
    else:
        print(f"There is a profiled named {userinpt} that is saved.")
        DecryptedPass = f.decrypt(EncryptedPass)
        print(f"{DecryptedPass}")
        
        





def DeleteProfile():
    userinpt = input("Profile to be deleted: ").strip()
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
print("WARNING: If two (or more) profiles have the same name THE LATEST PROFILE CREATED WILL BE KEPT WHILE THE OTHER WILL GET DELTED")
while Flag:
    print("----------------------------------")
    print("options are: SHOW, GET, DELETE, SAVE, NEW, EXIT")
    CMD = input("> ")
    CMD = CMD.upper().strip()
    if CMD == 'NEW':
        NewProfile()
    elif CMD == 'SAVE':
        SaveNewProfile()
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
    elif CMD == "EXIT":
        UserInput = input("Are you sure you want to quit? ( y / n ): ")
        if UserInput in ('yes' , 'y'):
            print("Exiting PmPy, all unsaved profiles will be deleted.")
            break
            quit()
        else:
            print("Did not exit.")
    else:
        print("Not valid command.")

