from colorama import init, Fore    
import os
print(Fore.RED + "Welcome To CE Editor!")
print("""1.Read File
2.Edit File
3.Create File And Edit""")
tools = int(input())
if tools == 1:
    print(Fore.GREEN + "File Name:")
    filename1 = str(input())
    with open(filename1, 'r') as readfile:
        print(readfile.read())
elif tools == 2:
    print(Fore.GREEN + "File Name:")
    filename2 = input()
    os.system(f"python3 editor.py {filename2}")
    exit()
elif tools == 3:
    print(Fore.GREEN + "File Name:")
    filename3 = input()

    os.system(f"python3 editor.py {filename3}")
    exit()