import socket
import platform
import requests
import hashlib
import time
from datetime import datetime

def banner():
    print("""
=================================
 CYBER TOOLKIT 10-IN-1
 Termux + Linux Ready
=================================
""")

def system_info():
    print("OS:", platform.system())
    print("Version:", platform.version())

def port_scanner():
    target = input("Target: ")
    try:
        ip = socket.gethostbyname(target)
    except:
        print("Invalid target")
        return

    print("Scanning:", ip)

    for port in range(20, 100):
        s = socket.socket()
        s.settimeout(0.2)

        if s.connect_ex((ip, port)) == 0:
            print("[OPEN]", port)

        s.close()

def website_check():
    url = input("URL: ")
    try:
        r = requests.get(url, timeout=5)
        print("STATUS:", r.status_code)
    except:
        print("DOWN")

def hash_tool():
    text = input("Text: ")
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

def menu():
    while True:
        print("""
1. System Info
2. Port Scanner
3. Website Check
4. Hash Tool
5. Exit
""")

        c = input("Choose: ")

        if c == "1":
            system_info()
        elif c == "2":
            port_scanner()
        elif c == "3":
            website_check()
        elif c == "4":
            hash_tool()
        elif c == "5":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    banner()
    menu()
