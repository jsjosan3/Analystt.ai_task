'''this code are used to create the new SQLite database to handle the data'''

import sqlite3

'''this is for creating a customer table which is used to 
    handle the customers details like name, mobile, email '''

try:
    conn = sqlite3.connect('rental.db')
    print ("rental.db database Opened  successfully")

    conn.execute('''CREATE TABLE Customer
            (NAME           TEXT    NOT NULL,
            MOBILE            INT     NOT NULL,
            EMAIL        CHAR(50));''')
    print ("Customer Table created successfully")

    conn.close()
except:
    print("Customer Table already exist")


'''this is for creating a Rental_Booking table which is used to 
    handle the details of  rental vehicles and inventory of vehicles '''

try:
    conn = sqlite3.connect('rental.db')
    print ("rental.db database Opened  successfully")

    conn.execute('''CREATE TABLE Rental_Booking
            (NAME           TEXT    NOT NULL,
            RENTAL_DATE     DATE     NOT NULL,
            RETURN_DATE     DATE,
            VEHICLE      CHAR(50));''')
    print ("Rental_Booking Table created successfully")
except:
    print("Rental_Booking Table already exist")