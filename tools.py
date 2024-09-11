#!bin/python

import os, sys, time
import random

# main menu
def menu():    
    os.system("clear")
    time.sleep(4)
    print("\033[0;31m*********************************")
    print("**  Tools By @peopleuniversal  **")
    print("**  Python Learning Language   **")
    print("**    Copyright@github.com     **")
    print("*********************************")
    time.sleep(3)
    print("\033[0;32m[1] Sharelock Location")
    print("[2] LITEDDOS")
    print("[3] SpiderBot")
    print("[4] LITETOOLS")
    print("[5] SpamBotOTP")
    print("[0] Exit")
    time.sleep(2)
    print("*********************************")
    tools = input("\033[0;30m[ Input Number ] >> ")

    # number 1
    if tools =="1":
        os.system("clear")
        print("\033[0;37mPlease wait for second!")
        time.sleep(2)
        os.system("clear")
        time.sleep(1)
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        os.system("clear")
        print("Done All Install...")
        time.sleep(2)
        os.system("clear")
        os.system("python tools.py")

    # number 2
    if tools =="2":
        os.system("clear")
        os.system("apt update && apt upgrade")
        os.system("pkg install git")
        os.system("pkg install python2")
        os.system("git clone https://github.com/4L13199/LITEDDOS")
        os.system("clear")
        print("Done All Install...")
        time.sleep(3)
        os.system("python tools.py")

    # number 3
    if tools =="3":
        os.system("clear")
        os.system("apt update && apt upgrade")
        os.system("apt install php")
        os.system("apt install git")
        os.system("git clone https://github.com/Cvar1984/SpiderBot.git")
        time.sleep(3)
        os.system("clear")
        time.sleep(3)
        print("Tinggal Dijalankan Saja, Seperti Hubunganmu Dengan Dia, Eaaa!:)")
        time.sleep(3)
        print("Contoh Saya Ingin Pakai Botkomen")
        time.sleep(3)
        print("Ketik: php botkoment.php")
        time.sleep(3)
        os.system("clear")
        os.system("python tools.py")
        
    # number 4
    if tools =="4":
        os.system("clear")
        os.system("pkg update && pkg upgrade")
        os.system("pkg install git")
        os.system("git clone https://github.com/4L13199/LITETOOLS")
        os.system("clear")
        print("Done All Install...")
        time.sleep(3)
        os.system("clear")
        os.system("python tools.py")
        
    # number 5
    if tools =="5":
        os.system("clear")
        print("pls wait for second...")
        time.sleep(2)
        os.system("apt update && apt upgrade -y")
        os.system("apt install python -y")
        os.system("git clone https://github.com/rickyfazaa/MySPAMBot-OTP")
        os.system("clear")
        print("Done All Install....")
        time.sleep(3)
        os.system("clear")
        os.system("python tools.py")

    # number exit(0)
    elif tools =="0":
        os.system("clear")
        print("Please Wait 3s...!!!")
        time.sleep(3)
        print("\033[0;32mBye Don't Forget Follow Media Social")
        time.sleep(2)
        os.system("exit")
        
    # command wrong!
    else:
        os.system("clear")
        print("\033[0;31mPls Input Number Valid...!!!")
        time.sleep(4)
        os.system("clear")
        os.system("python tools.py")
        
menu()
