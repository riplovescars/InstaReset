from colorama import Fore, init
from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits
)
import requests
import subprocess

# initing and clearing the screen
init(autoreset=True)
subprocess.run(['cls||clear'], shell=True)

# showing startup ascii art
print(Fore.MAGENTA + """
 ___           _          ____                _   
|_ _|_ __  ___| |_ __ _  |  _ \ ___  ___  ___| |_ 
 | || '_ \/ __| __/ _` | | |_) / _ \/ __|/ _ \ __|
 | || | | \__ \ || (_| | |  _ <  __/\__ \  __/ |_ 
|___|_| |_|___/\__\__,_| |_| \_\___||___/\___|\__|

[*] Version: v1.0
[*] Instagram: @kh.pythonista
[*] GitHub: https://github.com/Kh4lidMD
""")

# asking for a method
print(Fore.BLUE + "[+] Please choose a method")
print("[1] Email")
print("[2] Username")
method = input("[>] Method: ")
if method == '1':
    method = 'user_email'
elif method == '2':
    method = 'username'
else:
    print(Fore.RED + "[-] Invalid method")
    exit()
print("\n", end='')

# asking for the target
print(Fore.BLUE + "[+] Please enter the target's " + method)
target = input("[>] " + method.capitalize() + ": ")
print("\n", end='')

# validating the target if it's a username
def invalid():
    print(Fore.RED + "[-] Invalid username")
    exit()
if method == 'username':
    target = target.lower()
    if '..' in target:
        invalid()
    if target.startswith('.') or target.endswith('.'):
        invalid()
    
    for char in target:
        if char not in ascii_lowercase + digits + '_.':
            invalid()

# generating a random 32 character csrf token
csrf = ''
for i in range(32):
    csrf += choice(ascii_lowercase + ascii_uppercase + digits)

# setting request data
data = {
    '_csrftoken': csrf,
    method: target
}

# setting request headers
headers = {
    'user-agent': "Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440)"
}

# sending the request
try:
    req = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/', data=data, headers=headers)
    json_data = req.json()

    # showing status
    print(Fore.BLUE + "[+] Request status preview")
    print("[+] Request sent, status code: " + str(req.status_code))
    print("[+] JSON: " + str(json_data) + "\n")

    # success
    if json_data['status'] == 'ok':
        print(Fore.GREEN + "[+] Success")
        print(Fore.GREEN + "[+] Password reset link sent")
        print(Fore.GREEN + "[+] " + json_data['toast_message'])
    
    # error
    else:
        print(Fore.RED + "[-] Error")
        print(Fore.RED + "[-] Instagram error: " + json_data['message'])
# no internet
except requests.ConnectionError:
    print(Fore.RED + "[-] Error")
    print(Fore.RED + "[-] Connection error")
    exit()

except requests.exceptions.Timeout:
    print(Fore.RED + "[-] Error")
    print(Fore.RED + "[-] Instagram took too long to respond")
    exit()

# exit prompt
print(Fore.RED + "\n[>] Enter to exit ", end='')
input()
