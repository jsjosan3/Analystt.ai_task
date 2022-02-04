'''import all required libraries'''

import sqlite3
import pandas as pd

'''this class is created for handling the rental bookings of vehicles '''

dic = {'bike': 2, 'cycle':3, 'car':1, "boat":2}     # initial inventory of vehicles
class Rental:
    def __init__(self):
        pass

    '''function for handle the rental bookings'''

    def bookings(self, name, rentdate, returndate, Vehical):
        if dic[Vehical] != 0:
            new_value=dic[Vehical]-1                   
            dic.update({Vehical : new_value})
            sqliteConnection = sqlite3.connect('rental.db')     # connect to rental.db database
            cursor = sqliteConnection.cursor()
            insert_with_param = """INSERT INTO Rental_Booking             
                              (NAME, RENTAL_DATE, RETURN_DATE,VEHICLE) 
                              VALUES (?, ?, ?,?);"""
                                                    # data added into the Rental_Booking table withe all info
            data_tuple = (name, rentdate, returndate, Vehical)
            cursor.execute(insert_with_param, data_tuple)
            sqliteConnection.commit()
            cursor.close()
            print(f"Booking of 1 {Vehical} is  confirmed")
            print(f"{dic} are avialable Vehicle in stock")
        else:
            print(f"all {Vehical} are alraedy booked")
            print(f"{dic} are avialable Vehicle in stock")

    '''function to display tha all rental details of vehicles '''

    def getRentalDetails(self):
        sqliteConnection = sqlite3.connect('rental.db')
        cursor = sqliteConnection.cursor()
        query = "SELECT * FROM Rental_Booking"
        df = pd.read_sql(query, sqliteConnection)
        print(df)
        sqliteConnection.commit()
        cursor.close()
    
    '''function to diplay the inventory of avialable Vehicles'''

    def inventory(self):
        df = pd.DataFrame(list(dic.items()), columns=("Vehicle", "Inventory"))
        return df

print("code exicuted successfully")