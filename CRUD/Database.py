"""
This module will initiate the database.
"""

from . import Operation
import time

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
        Operation.create_first_data()      

       
            
    