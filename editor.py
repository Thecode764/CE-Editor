import keyboard
import sys
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)
run = True
if len(sys.argv) == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    fname = sys.argv[1]
    print(Back.WHITE+Fore.BLACK+"Thecode764 editor [version 0.1]")
    print(Back.WHITE+Fore.BLACK+"(C)Thecode. all rights reserved")
    print(Back.WHITE+Fore.BLACK+f"File: {fname}")
    try:
        while True:
            t = input("")
            with open(fname, "a") as f:
                f.write(f"{t}\n")
    except EOFError:
        print("EOF Error")
    except KeyboardInterrupt:
        print("")
        with open(fname,"r") as l:
                ln = len(l.readlines())
        print(Back.WHITE+Fore.BLACK+f"saved {ln} lines in {fname} ")
        exit()
else:
    print(Back.WHITE+Fore.BLACK+"Thecode764 editor [version 0.1]")
    print(Back.WHITE+Fore.BLACK+"(C)Thecode. all rights reserved")
    print(f"USAGE: python3 {sys.argv[0]} <file_name>")