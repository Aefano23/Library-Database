"""
This module will take the user's input related to CRUD process.
"""
from . import Operation

def create_console():
    """
    Function to take the new book info from the user
    """
    while(True):
        #Take input from user
        print("\n\n"+"="*100)
        print("Please insert your book info\n")
        title = input("Title\t: ")
        author = input("Author\t: ")
        while(True):
            try:
                year = int(input("Year\t: "))
                if len(str(year)) == 4:
                    break
                else:
                    print('Year must be four digits (YYYY)')
            except:
                print('Year must be number (YYYY)')
        
        #Show the user's input
        print('New book entry')
        print(f'1. Title\t: {title:.40}')
        print(f'2. Author\t: {author:.40}')
        print(f'3. Year\t: {year:4}')   

        #Confirmation message for saving the input
        is_done = input("Save this book (y/n): ")
        if is_done.lower() == 'y':
            Operation.create(title,author,year)
            print("\nNew book entry has been added to the database.")

        #Confirmation message for back to main menu
        back = input("Back to main menu? (y/n): ")
        if back.lower() == 'y':
            break


def read_console(): 
    """
    Function to show the book data when the users choose option 3 or 4 on the main program (Base.py) 
    """
    data_file =  Operation.read() #calling the read function from Operation module to read Database
    
    # Defining variables for header
    index = 'No'
    title = 'Title'
    author = 'Author'
    year = 'Year'

    # Show header
    print('\n'+'='*100)
    print(f'{index:4} | {title:40} | {author:40} | {year:5}')
    print('-'*100)
    
    # Show Data
    for index, data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_added = data_break[1]
        title = data_break[2]
        author = data_break[3]
        year = data_break [4]   
        print(f'{index+1:4} | {title:.40} | {author:.40} | {year:4}',end="")
    
    # Show footer
    print('='*100+'\n')

    
def show_console(): 
    """
    Function to show the book data when the users choose option 1 on the main program (Base.py) 
    """
    while (True):
        read_console()

        back = input("Back to main menu? (y/n): ")
        if back.lower() == 'y':
            break
    

def update_console():
    """
    Function to take input from the user for updating the book data
    """
    while(True):
        read_console()
        print("Please select the book number that need to be update: ")
        book_number = int(input('Book Number: '))
        book_data = Operation.read(index=book_number)
         
        if book_data:
            data_break = book_data.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            title = data_break[2]
            author = data_break[3]
            year = data_break [4][:-1]    
    
            while(True):
                print('\n'+'='*100)
                print('Select the book data that need to be change')
                print(f'1. Title\t: {title:.40}')
                print(f'2. Author\t: {author:.40}')
                print(f'3. Year\t: {year:4}')

                user_option = input("Your Option [1,2,3]: ")
                print('\n'+'='*100)

                match user_option: 
                    case "1": title = input('Title\t: ')
                    case "2": author = input('Author\t: ')
                    case "3":
                        while(True):
                            try:
                                year = int(input("Year\t: "))
                                if len(str(year)) == 4:
                                    break
                                else:
                                    print('Year must be four digits (YYYY)')
                            except:
                                print('Year must be number (YYYY)')
                    case _: print('Invalid Input')

                print('Your new data')
                print(f'1. Title\t: {title:.40}')
                print(f'2. Author\t: {author:.40}')
                print(f'3. Year\t: {year:4}')   
        
                is_done = input("Done Updating? (y/n): ")
                if is_done.lower() == 'y':
                    Operation.update(book_number,pk,data_add,title,author,year)
                    print('Book data has been updated.')
                    break

        else:
            print('Invalid number, please try again')
        
        back = input("Back to main menu? (y/n): ")
        if back.lower() == 'y':
            break  

    
def delete_console():
    """
    Function to delete the book from database based on user's input
    """
    while(True):
        read_console()
        print("Please select the book number that need to be delete: ")
        book_number = int(input('Book Number: '))
        book_data = Operation.read(index=book_number)

        if book_data:
            data_break = book_data.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            title = data_break[2]
            author = data_break[3]
            year = data_break [4][:-1] 

            print('\n'+'='*100)
            print('Book that will be deleted:')
            print(f'1. Title\t: {title:.40}')
            print(f'2. Author\t: {author:.40}')
            print(f'3. Year\t: {year:4}')
            is_done = input("Confirm delete? (y/n): ")
            if is_done == 'y' or is_done == 'Y':
                Operation.delete(book_number)
                print("Book has been deleted successfully.")
        else:
            print('Invalid number, please try again')

        back = input("Back to main menu? (y/n): ")
        if back.lower() == 'y':
            break

    
    
    
        
       
        

