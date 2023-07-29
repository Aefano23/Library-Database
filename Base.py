"""
Basic CRUD Program

Study Case : Library Database
Description : Applying CRUD to an external file (.txt)
Author : Aditya Efano Putra
Reference : Python 3.x Tutorial by Kelas Terbuka Youtube Channel

This is the main program. This program is act as a "gate" of overall programs.
"""

import os 
import CRUD as CRUD

#Executing the OS matching if this program executed directly.
if __name__ == "__main__": 
    operating_system = os.name
    
    #Checking the existence of the Database.
    CRUD.init_console()
    
    while(True):
        match operating_system: #OS matching to clear terminal when executing the program.
            case "posix" : os.system('clear') #matching OS linux/unix.
            case "nt" : os.system('cls') #matching OS windows.

        #Header
        print('BOOK COLLLECTION DATABASE')
        LibName = "OHARA LIBRARY".center(23)
        print(" "+LibName+" ")
        print('=========================')

        #List of available input.
        print(f"1. Show books")
        print(f"2. Insert new book")
        print(f"3. Update book data")
        print(f"4. Remove book")
        print(f"5. Exit App\n")

        user_option = input("Select action: ") #take input from user.

        match user_option: #matching the user's input to available command.
            case "1": CRUD.show_console() 
            case "2": CRUD.create_console() 
            case "3": CRUD.update_console() 
            case "4": CRUD.delete_console() 
            case "5": 
                exit = input("Are you sure want to exit? (y/n): ")
                if exit.lower() == 'y':
                    break
                    
    print("\nThank you for using this app\n") #end of program.

        






