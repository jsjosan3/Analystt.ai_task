'''import created modules'''

from customer import Customer   
from rental import Rental

'''created function to add the customers details by the user'''

def enterDetails():
    name= input("Enter Customer Name: ")
    mob = int(input("Enter Mobile Number: "))
    email = input("enter email id: ")
    cust=Customer()
    cust.addDetails(name,mob,email)

'''function to view the customers list present in database'''

def customerList():
    cust= Customer()
    return cust.getDetails()

'''function to do the renatal bookings by users after input the details '''

def rentalBooking():
    name= input("Enter Customer Name: ")
    rent_date = input("Date of Booking: ")
    return_date = input("Return Date: ")
    Vehicle = input("Vehicle Kind   (1.bike 2.cycle 3.car 4.boat): ")
    rent=Rental()
    rent.bookings(name,rent_date, return_date, Vehicle)

'''to view the list of rental bookings of vehicles'''

def bookingDetails():
    rent=Rental()
    return rent.getRentalDetails()

'''function to view the avaialble invntory of vehicles'''

def inventorylist():
    rent=Rental()
    data=rent.inventory()
    print(data)

'''created a menu fo different tasks'''

menu = {}
menu['1'] = "Add Customer." 
menu['2'] = "Customer List."
menu['3'] = "Add Rental Booking"
menu['4'] = "Rental booking list"
menu['5'] = "See inventory of vehicles available"
menu['6'] = "Exit"
while True:                         #by using while loops application run continuesly in shell
    print ("1.Add a Customer")
    print("2.Show customer List")
    print("3.Add Rental Booking")
    print("4.Rental booking list")
    print("5.See inventory of vehicles available")
    print("6.Exit/Quit") 
    options=menu.keys()
    #options.sort()
    for entry in options: 
        entry, menu[entry]

    selection=input("Please Select:") 
    if selection =='1':
        enterDetails()
    elif selection == '2': 
        customerList()
    elif selection == '3': 
        rentalBooking()
    elif selection == '4': 
        bookingDetails()
    elif selection == '5':
        inventorylist()
    elif selection == '6': 
        break
    else: 
      print ("Unknown Option Selected!") 


