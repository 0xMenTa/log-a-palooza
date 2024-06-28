log-a-palooza.py

█░░ █▀█ █▀▀ ▄▄ ▄▀█ ▄▄ █▀█ ▄▀█ █░░ █▀█ █▀█ ▀█ ▄▀█ ░ █▀█ █▄█
█▄▄ █▄█ █▄█ ░░ █▀█ ░░ █▀▀ █▀█ █▄▄ █▄█ █▄█ █▄ █▀█ ▄ █▀▀ ░█░

This is a Python learning project. The basic idea is to create a keylogger software in Python that captures keystrokes on a victim's PC. This keylogger is also connected to a Discord server via a webhook, allowing it to send the victim's inputs to a dedicated discussion channel.

Here are the steps to build the project:
	- Create a script that captures keyboard keystrokes and logs them during a session. ✓
	- Store the inputs in a file named evidence.log. ✓
	- The evidence.log file is created in a randomly named folder on the victim's desktop. ✓
	- Once the basic keylogger script works perfectly, the next step is to connect it to a Discord webhook on a server.
	- Find a way to send the inputs to channels created with the name of the PC, a date, and a random string of characters.

Further steps to be determined later...
Note to self: Send the inputs each time the user presses "space" or "enter"?"

UPDATE 28/06/2024 : The core of the keylogger seem to be done, The script is able to capture keystrokes from the keyboard and It can also interpret "Enter" and "Space" keystrokes in order to create a space or a line break and thus provide clearer data when the attacker reads the inputs. Now i want to create the random directory and a log file Which may seem legit.

UPDATE 28/06/2024 : The processus of creating a random directory and a fake legit file created inside it is done. the file is like "AVAST-Security-Check-[DATE]-[XXX] XXX for 3 randoms number (In case if the script is launched many times on same day). When I launch the script : Directory is created with random UUID4 -> a txt file -> the script capture all inputs, if its enter we write \n and if its space we write " ". All is made on Linux so we need to adapt that for Windows. My next goal is test it with a real firefox session but my VM crashed :/
