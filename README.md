# log-a-palooza.py

█░░ █▀█ █▀▀ ▄▄ ▄▀█ ▄▄ █▀█ ▄▀█ █░░ █▀█ █▀█ ▀█ ▄▀█ ░ █▀█ █▄█
█▄▄ █▄█ █▄█ ░░ █▀█ ░░ █▀▀ █▀█ █▄▄ █▄█ █▄█ █▄ █▀█ ▄ █▀▀ ░█░

This is a Python learning project. The basic idea is to create a keylogger software in Python that captures keystrokes on a victim's PC. This keylogger is also connected to a Discord server via a webhook, allowing it to send the victim's inputs to a dedicated discussion channel.

Here are the steps to build the project:
1 - Create a script that captures keyboard keystrokes and logs them during a session.
2 - Store the inputs in a file named evidence.log.
3 - The evidence.log file is created in a randomly named folder on the victim's desktop.
4 - Once the basic keylogger script works perfectly, the next step is to connect it to a Discord webhook on a server.
5 - Find a way to send the inputs to channels created with the name of the PC, a date, and a random string of characters.

Further steps to be determined later...
Note to self: Send the inputs each time the user presses "space" or "enter"?"
