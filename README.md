# Analystt.ai_task
#### Task Info
* creating a simple python app to manage the rental of bikes and scooters for a small start-up. The app will be used by the employees of the startup to manage their vehicles and rentals.You can complete this task either by using some web frameworks like (Django or FastAPI) OR Class-Object
* Following vehicles, are available for rental. 

{‘vehicle_type’: inventory}

{‘bikes’:2, ‘cycle’:3, ’car’:1, ’boat’:2} 

The employees can add customers, add rental bookings,view customer list, view rental bookings, and view inventory.
* While making a new rental booking, the app needs to check, whether the vehicle is there in the inventory, if yes, the enter in the database, and reduce the inventory by 1. If not, then a message can be shown “{vehichle} cannot be rented as it is already booked”

#### Solution
* the aap is made by using the Class object method
* For Classes, Objects, Inheritance
• Use python shell, which displays menu, asks user
     1. Add customer
     2. Add rental booking
     3. See customer list
     4. See rental booking list
     5. See inventory of vehicles available
• Once the user selects an option, relevant operation needs to be displayed
• Predefine the vehicle list in dictionary or list

#### Workflow 
     * first download all python file and requirements.txt from repository
     * place all the file in one director(folder)
     * creat a virtual envoirnment (recomanded: anaconda env)
     * avtivate env.
     * install  requirements.txt ("pip install -r requirements.txt")
     * first run dbhandel.py, which create  a new sqlite database with two Tables name Customer and Rental_Booking
     * second run main.py, to run the app in python shell
     * select option as required for operation
