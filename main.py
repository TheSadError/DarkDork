from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import os
from colorama import Fore,Back,Style
import sys
import time

def banner():
    print(Fore.RED+"""
     ___                 _      ___                 _     
    (  _`\              ( )    (  _`\              ( )    
    | | ) |   _ _  _ __ | |/') | | ) |   _    _ __ | |/') 
    | | | ) /'_` )( '__)| , <  | | | ) /'_`\ ( '__)| , <  
    | |_) |( (_| || |   | |\`\ | |_) |( (_) )| |   | |\`\ 
    (____/'`\__,_)(_)   (_) (_)(____/'`\___/'(_)   (_) (_)                                                                                  
    """)

os.system("clear") #if you use windows put cls instead of clear
banner()
if sys.version[0] in "2":
    print ("\n[!] Srry... You must use python3 to run DarkDork! You are using python2. Please retry to run code.\n")
    exit()


y = "May you answear my questions ?"

z = "\n"
for col in z:
    print(Fore.BLUE + col, end="")
    sys.stdout.flush()

try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print (Fore.RED+"[!] User Interruption Detected..!")
        time.sleep(0.5)
        print (Fore.RED+"[!] I like to See Ya, Hacking 😃.")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y" or "yes" or "Yes"):
    l0g = input(Fore.GREEN+"[-] Give The File a Name: ")
    time.sleep(1)
    logger(data)
else:
    print(Fore.RED+"[!] Saving is Skipped...")
    time.sleep(1)


def dorks():
    try:
        dork = input(Fore.BLUE+"\n[+] Enter The Dork Search Query: ")
        amount = input(Fore.BLUE+"[+] Enter The Number Of Websites To Display: ")

        requ = 0
        counter = 0
        print(Fore.BLUE+"[+] Results : ")
        print("")
        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print (f"[+][{counter}]", results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

        print("")
        
    except KeyboardInterrupt:
            print ("\n")
            print (Fore.RED+"[!] User Interruption Detected..!")
            time.sleep(0.5)
            print (Fore.RED+"[!] Bye Bye! Thanks to use DarkDork!")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print (Fore.RED+"[!] I like to See Ya, Hacking...")
    sys.exit()


if __name__ == "__main__":
    dorks()
