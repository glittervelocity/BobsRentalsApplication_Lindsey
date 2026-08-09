# BobsRentals_EF
## Include a README containing:
### •	Your name
Classes written by Emily Fischer
### •	Course name
This program was written for my Object-Oriented Programming course @ Cstate
### •	A brief description of your design
This design will include a handful of classes for the prompt of Bob's Ski & Snowboard Rental / Hotel Co. providing the framework for methods to be written next week to calculate various statistics.
### •	A list of your classes
RentalEquipment (rental_equipment.py)

Abstract parent class representing any rentable equipment. Defines shared properties and methods for skis and snowboards.\

Ski (ski.py)\

Inherits from RentalEquipment. Represents ski equipment with preset rates: $15/hr, $50/day, $200/week.\

Snowboard (snowboard.py)\

Inherits from RentalEquipment. Represents snowboard equipment with preset rates: $10/hr, $40/day, $160/week.\

Customer (customer.py)\

Stores customer name and ID. Validates that name is not empty and ID is greater than 0.\

Rental (rental.py)\

Represents a single rental transaction. Handles pricing, discount logic, estimates, and final billing.\

RentalShop (rental_shop.py)\

Manages equipment inventory and tracks daily totals for skis rented, snowboards rented, and total revenu\

### •	An explanation of the important properties and methods available to the application programmer
RentalEquipment / Ski / Snowboard\
Property / Method	Description\
name	Equipment type name\
hourly_rate	Cost per hour\
daily_rate	Cost per day\
weekly_rate	Cost per week\
available_inventory	Current number of items available\
starting_inventory	Original inventory count set at startup\
rent(quantity)	Reduces available inventory; raises exception if insufficient\
return_equipment(quantity)	Restores inventory on return\
get_best_price(hours)	Returns the lowest available rate for the given number of hours\
describe()	Displays equipment details (abstract — implemented by Ski and Snowboard)\
\
Customer\
Property	Description\
name	Customer's name — must be at least 1 character\
customer_id	Unique ID — must be greater than 0\
\
Rental\
Property / Method	Description\
customer	The Customer object for this rental\
equipment	The RentalEquipment object being rented\
quantity	Number of items rented (1–5)\
hours	Rental duration in hours\
coupon_code	Optional coupon code\
calculate_estimate()	Returns estimated cost before renting begins\
calculate_final_bill()	Returns final cost when equipment is returned\
\
RentalShop\
Property / Method	Description\
set_inventory(ski, snowboard)	Sets starting inventory for both equipment types\
display_available()	Displays current available inventory\
process_rental(rental)	Reduces inventory and records daily totals\
process_return(rental)	Restores inventory and returns final bill\
display_daily_totals()	Displays skis rented, snowboards rented, and total revenue\
## •	An explanation of where you used: 
### o	Encapsulation
All class attributes are stored as private variables using the underscore convention (_name, _hourly_rate). Public access is controlled through @property getters and setters, which validate values before storing them and raise descriptive exceptions when invalid data is provided.
### o	Inheritance
Ski and Snowboard both inherit from RentalEquipment, sharing common attributes (rates, inventory, pricing logic) while providing their own preset rate values and describe() implementations. This avoids code duplication and makes the library easy to extend with new equipment types.
### o	Polymorphism
Both Ski and Snowboard override the describe() method from RentalEquipment, providing type-specific output while sharing the same interface. This allows an application programmer to call describe() on any equipment object without knowing its specific type.
### o	Abstraction
RentalEquipment is defined as an abstract base class using Python's ABC module. The describe() method is marked as @abstractmethod, meaning it cannot be instantiated directly and any subclass must provide its own implementation. This enforces a consistent interface across all equipment types.
## •	Instructions for running your testing file
Clone the repository\
Open the files in Visual Studio\
Run the testing file:\
python test_main.py
