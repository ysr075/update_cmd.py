import os
import time
import random

def timer(seconds = 0.125):
    time.sleep(seconds)

def color():
    num = random.randint(1,9)
    os.system("color 0" + str(num))

def clear():
    os.system("cls")

def new_line():
    print("\n")

def loading():
    print("developed by @ysr075\n  <    loading.")
    timer()
    color()
    clear()
    print("developed by @ysr075\n  <|   loading..")
    timer()
    color()
    clear()
    print("developed by @ysr075\n  <|>  loading...")
    timer()
    color()
    clear()
    print("developed by @ysr075\n    >  loading...")
    timer()
    color()
    clear()
    print("developed by @ysr075\n   |>  loading..")
    timer()
    color()
    clear()
    print("developed by @ysr075\n  <|>  loading.")
    timer()
    color()
    clear()

def directory():
    os.system("dir")

def ipconfig():
    os.system("ipconfig")

def pinging():
    ip_req = str(input("victim ip: "))
    os.system("ping " + ip_req)
    new_line()

def main():
    while True:
        shell = input("root@ysr075:~# ")
        if shell == "wifikey" or shell == "wifikeyprofile":
            os.system("netsh wlan show profiles")
            wifi_name = str(input("wifi victim: "))
            os.system("netsh wlan show profiles " + wifi_name + " key=clear")
        elif shell == "clear" or shell == "cls":
            clear()
        elif shell == "ls" or shell == "dir":
            directory()
        elif shell == "ifconfig":
            ipconfig()
        elif shell == "ping":
            pinging()

for i in range(0, 3):
    loading()
main()
