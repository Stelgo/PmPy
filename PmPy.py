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
    tempdict.update({f"{Profile}" : PF_Password})
    print("New profile created.")
    return tempdict
    
def SaveNewProfile():
    global tempdict
    while True:
        userinpt = input("Are you sure you want to save? (y / n)")
        userinpt = userinpt.lower().strip()
        if userinpt in ("y", "yes"):
            print("Profile saved.")
            tempRender = json.dumps(tempdict)
            with open("PasswordPmPy.json", "a", encoding="utf-8") as File:
                File.write(json.dumps(tempRender, ensure_ascii=False) + "\n")
            time.wait(2)
            break
        elif userinpt in ("n" , "no"):
            print("Aborted. (Did not save the file)")
            break
        else:
            print("Wrong input try again")
            global y
            y += 1
            if y == 3:
                choise = input("Do you want to Abort? (y / n) ")
                if choise in ("y", "yes"):
                    y = 0
                    break
                elif choise in ("n" , "no"):
                    y = 0
                    pass


def LoadStoredProfiles():
    global masterdict
    try:
        with open("PasswordPmPy.json", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)          
                masterdict.update(obj)        
    except FileNotFoundError:
        with open("PasswordPmPy.json", "w", encoding="utf-8") as f:
            f.close()


def GetProfile():
    global masterdict
    global tempdict
    global f
    userinpt = input("Enter profile name: ")
    userinpt = userinpt.strip()
    print(f"Saved profiles with the name: {userinpt} ")
    try:
        UncryptedSaved = masterdict.get(userinpt)
        temp = f.decrypt(UncryptedSaved)
        UncryptedSaved = temp
        print('')
        print(UncryptedSaved)
    except TypeError:
        print('')
        print(f"No saved profiles with the  name: {userinpt} ")
    print('')
    print("-----------------------------------------------------")
    print('')
    print(f"Not saved profiles with the name: {userinpt} ")
    try:
        UncryptedTemp = tempdict.get(userinpt)
        temp = f.decrypt(UncryptedTemp)
        UncryptedTemp = temp
        print('')
        print(UncryptedTemp)
    except TypeError:
        print('')
        print(f"No not saved profiles with the  name: {userinpt} ")
    
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

