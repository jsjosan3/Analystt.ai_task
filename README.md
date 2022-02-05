# Analystt.ai_task
#### Task Info
* creating a simple python app to manage the rental of bikes and scooters for a small start-up. The app will be used by the employees of the startup to manage their vehicles and rentals. You can complete this task either by using some web frameworks like (Django or FastAPI) OR Class-Object
* Following vehicles, are available for rental. 

{‘vehicle_type’: inventory}

{‘bikes’:2, ‘cycle’:3, ’car’:1, ’boat’:2} 

The employees can add customers, add rental bookings, view customer lists, view rental bookings, and view inventory.
* While making a new rental booking, the app needs to check, whether the vehicle is there in the inventory, if yes, the entry in the database, and reduce the inventory by 1. If not, then a message can be shown “{vehichle} cannot be rented as it is already booked”

#### Solution
* the app is made by using the Class object method
* For Classes, Objects, Inheritance, here I used python shell, which displays a menu, asks the user
     1. Add customer
     2. Add rental booking
     3. See customer list
     4. See rental booking list
     5. See an inventory of vehicles available
• Once the user selects an option, the relevant operation displayed
• used Predefined the vehicle list in dictionary or list

#### Workflow 
     * First download all python files and requirements.txt from the repository
     * place all the files in one directory(folder)
     * create a virtual environment (recommended: anaconda env)
     * activate env.
     * install  requirements.txt ("pip install -r requirements.txt")
     * First run dbhandel.py, which create  a new SQLite database with two Tables name Customer and Rental_Booking
     * second run main.py, to run the app in python shell
     * Select option as required for operation

