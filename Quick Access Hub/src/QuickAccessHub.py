import subprocess as sp
import time


def runCommand():
    username = "Admin"
    password = "Hbq123Phobetor??"
    attempts = 0
    lockoutTime = 30  # seconds

    while attempts < 3:
        userName = input("Username: ")
        userPassword = input("Password: ")

        if userPassword == password and username == userName:
            while True:
                print("****QUICK ACCESS HUB****")
                choice = input("1. Notepad\n2. Git-bash\n3. Calculator\n4. Edge\n5. Exit\n")

                try:
                    if choice == "1":
                        sp.call(["notepad.exe"])
                        input("Do you want to continue?")
                        
                    elif choice == "2":
                        sp.call(["C:\\Program Files\\Git\\git-bash.exe"])
                        input("Do you want to continue?")
                        
                    elif choice == "3":
                        sp.call(["calc.exe"])
                        input("Do you want to continue?")
                        
                    elif choice == "4":
                        sp.call(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
                        input("Do you want to continue?")
                        
                    elif choice == "5":
                        print("Exiting the app")
                        break
                    
                    else:
                        print("Invalid choice. Please choose a valid option.")
                except FileNotFoundError as err:
                    print(f"Error: {err}")
                    break               # Exit the inner loop if there's an error
        else:
            attempts += 1
            print("Incorrect password or username. Please try again")

            if attempts == 3:
                print(f"Too many attempts. Locking out for {lockoutTime} seconds")
                time.sleep(lockoutTime)

runCommand()