"""
This module will initiate the database and conducting the CRUD operation.
"""

from . import Util
import time
import shutil


#Define database format.
DB_NAME = 'bookdata.txt'
COLUMN = {
    "pk" : "XXXXXX",
    "date_added" : "dd-mm-yyyy",
    "title" : 255*" ",
    "author" : 255*" ",
    "year" : "yyyy"
}


def init_console():
    """
    Function for check the database. If it exist, the program will read the database.
    If not, the program will create the new database.
    """
    print('Checking database...')
    time.sleep(1.5)
    try:
        with open(DB_NAME,'r') as file:
            print('Database exist')
            time.sleep(0.7)
    except:
        print("Database doesn't exist. Create new database")
        create_first_data()      


def delete(book_number):
    """
    Function for Delete Operation
    """
    try:
        with open(DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == book_number - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database Error")

    shutil.move('data_temp.txt',DB_NAME)


def create(title,author,year):
    """
    Function for Create Operation
    """
    data = COLUMN.copy()
    
    data['pk'] = Util.random_string(6)
    data['date_added'] = time.strftime("%d-%m-%Y %H:%M%z",time.gmtime())
    data['title'] = title + COLUMN["title"] [len(title):]
    data['author'] = author + COLUMN["author"] [len(author):]
    data['year'] = str(year)

    data_str = f"{data['pk']},{data['date_added']},{data['title']},{data['author']},{data['year']}\n"
    try:
        with open(DB_NAME,'a', encoding= 'utf-8') as file:
            file.write(data_str)
    except:
        print('Error while adding new entry')


def create_first_data():
    """
    Function to take the user's input for the new database's attribute
    """
    title = input('Title\t: ')
    author = input('Author\t: ')
    while(True):
        try:
            year =  int(input('Year\t: '))
            if len(str(year)) == 4:
                break
            else:
                print('Year must be four digits (YYYY)')
        except:
            print('Year must be four digits (YYYY)')


    data = COLUMN.copy()
    
    data['pk'] = Util.random_string(6)
    data['date_added'] = time.strftime("%d-%m-%Y %H:%M%z",time.gmtime())
    data['title'] = title + COLUMN["title"] [len(title):]
    data['author'] = author + COLUMN["author"] [len(author):]
    data['year'] = str(year)

    data_str = f"{data['pk']},{data['date_added']},{data['title']},{data['author']},{data['year']}\n"
    print(data_str)
    try:
        with open(DB_NAME,'w', encoding= 'utf-8') as file:
            file.write(data_str)
    except:
        print('Error while creating database')


def read(**kwargs): 
    """
    Function for Read Operation
    """
    try:
        with open(DB_NAME,'r') as file:
            content = file.readlines()
            total_book = len(content) #Content is list, so the length of content is the total amount of books
            if "index" in kwargs:
                book_index = kwargs['index']-1
                if book_index < 0 or book_index > total_book:
                    return False
                else:
                    return content[book_index]
            else:   
                return content
                  
    except:
        print("Error while reading database")
        return False


def update(book_number,pk,data_add,title,author,year):
    """
    Function for Update Operation
    """
    data = COLUMN.copy()
    
    data['pk'] = pk
    data['date_added'] = data_add
    data['title'] = title + COLUMN["title"] [len(title):]
    data['author'] = author + COLUMN["author"] [len(author):]
    data['year'] = str(year)
    
    data_str = f"{data['pk']},{data['date_added']},{data['title']},{data['author']},{data['year']}\n"
    
    try:
        with open(DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == book_number - 1:
                    with open("update_temp.txt",'a',encoding="utf-8") as update_file:
                        update_file.write(data_str)
                else:
                    with open("update_temp.txt",'a',encoding="utf-8") as update_file:
                        update_file.write(content)
                counter += 1
    except:
        print("Error while updating book data")

    shutil.move('update_temp.txt',DB_NAME)
      
            
    