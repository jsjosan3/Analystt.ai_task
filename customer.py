'''import all required libraries'''
 
import sqlite3
import pandas as pd

'''this class is created for handling the customers data '''

class Customer:
    def __init__(self):
        pass
    
    '''function to add the new customers in database '''

    def addDetails( self,name, mob, email):
        sqliteConnection = sqlite3.connect('rental.db')   # data added to the rental.db using SQLite 
        cursor = sqliteConnection.cursor()
        insert_with_param = """INSERT INTO Customer
                          (NAME, MOBILE, EMAIL) 
                          VALUES (?, ?, ?);"""

        data_tuple = (name, mob, email)
        cursor.execute(insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Customer added successfully")
        cursor.close()
        

    '''Function to show the list of customers which are previously added into the database'''

    def getDetails( self):
        sqliteConnection = sqlite3.connect('rental.db') #connect to rental.db database
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT * FROM Rental_Booking")
        query = "SELECT * FROM Customer"
        df = pd.read_sql(query, sqliteConnection)  # customers data viewed to user in the form of dataframe
        print(df)
        sqliteConnection.commit()
        cursor.close()

print("code exicuted successfully")