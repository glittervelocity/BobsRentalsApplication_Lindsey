#################################
## Bryanna Lindsey Final part 2: application 
#################################


#################################
## Pulling in all the classes
#################################

from Ski import ski
from Snowboard import snowboard
from Customer import customer
from Rental import rental
from RentalShop import rental_shop
from datetime import datetime

#################################
## Before we set up the shop we validate the inputs. I didn't see a good way to do this in the classes but maybe I missed something
#################################

def validate_value(prompt):
    while True:
        num = input(prompt)
        value = int(num)
        if value < 0: 
                print ("Number should be greater than 0")
                continue 
        return value 

###############################
## Generate the main menu  
################################# 

def get_menu_choice():
    print("\n Bob's Rentals Main Menu:")
    print("1. New Customer Rental")
    print("2. Rental Return")
    print("3. Show Inventory")
    print("4. End of Day")
    return input("Enter menu choice: ")


def get_rental_period_hours():
    return validate_value("Enter rental hours: ")


#################################
## This is the initial set up for the shop and get inventory
#################################

def start_application():
    print ("Bob's ski rentals initial shop set up:")

    while True: 
        starting_skis = validate_value("Enter starting ski number: ")
        starting_snowboards = validate_value("Enter starting snowboard number: ")
        break 

    shop = rental_shop()
    shop.set_inventory(ski(starting_skis), snowboard(starting_snowboards))

    active_rentals = {}
    ## I couldn't quite get the class method to work for this. Maybe I was doing something wrong there
    daily_stats = {
        "Total skis rented": 0,
        "Total snowboards rented": 0,
        "Total revenue": 0.0,
    }
    main_menu(shop, active_rentals, daily_stats, shop.display_available)

#################################
## This is where we run our main menu
#################################

def main_menu(shop, active_rentals, daily_stats, display_available):
    while True:
        choice = get_menu_choice()

        if choice == "1":
            new_rental(shop, active_rentals, daily_stats, display_available)
        elif choice == "2":
            rental_return(shop, active_rentals, daily_stats, display_available)
        elif choice == "3":
            ## Use the shop class avalible. This gives me an error sometimes, and I don't know why. Tried to debug it 
            shop.display_available()
        elif choice == "4":
            ## use the shop daily totals 
            shop.display_daily_totals()
            print ("Day complete, closing application")
            break 
        else: 
            print ("Not a valid choice, please select 1, 2, 3, or 4")

#################################
## This is a process for processing a new rental 
#################################
 
def new_rental(shop, active_rentals, daily_stats):
    print ("\n -- New Customer Rental Menu --")

    customer_id = validate_value("Enter customer's ID: ")
    customer_name = input("Enter customer's name: ")

## Select ski or snowboard 
    eq_choice = input("Rent Ski (1) or Snowboard (2)? ")
    
    quantity = None 
    if eq_choice == "1":
       equipment_obj = shop._ski_inventory

    elif eq_choice == "2":
        equipment_obj = shop._snowboard_inventory

## Check equipment rental with the inventory 
    while True:
       quantity = validate_value("Enter number of rentals 1-5: ")
       if quantity > 5: 
          print("Rental number cannont exced 5")
          continue 
       if quantity > equipment_obj.available_inventory: 
          print (f"Not enough inventory available. Requested {quantity}, Available {equipment_obj.available_inventory}")
          continue 
       break

    hours = get_rental_period_hours()

## add coupon functionality 
    coupon_code = input("Coupon code? (optional, press Enter to skip): ")
    if coupon_code == "":
        coupon_code = ""

## add objects to track equipment and customers 
    cust = customer(customer_name, customer_id)
    rental_obj = rental(cust, equipment_obj, quantity, hours)

## show estimates 
    estimate = rental_obj.calculate_estimate()
    print (f"Rental estimate: ${estimate}")

    confirm = input("Complete this rental? (Yes/No): ")
    if confirm not in ("yes", "Yes", "y"):
       print("Rental cancelled")

## Reduce inventory + upadate daily totals 
    cost = shop.process_rental(rental_obj)

## Daily stats
    if equipment_obj.name == "Ski":
       daily_stats["Total skis rented"] += quantity 
    else: 
       daily_stats["Total snowboards rented"] += quantity 
    daily_stats["Total revenue"] += cost

    active_rentals[customer_id] = rental_obj
    print ("Rental completed successfully!")

    
#################################
## This is a process for rental returns 
#################################

def rental_return(shop, active_rentals, daily_stats):
    print ("-- Rental Return --")
    
    ##check if there is a rental for the customer 
    customer_id = validate_value("Enter customer ID: ")

    if customer_id not in active_rentals:
       print ("No active rentals for this customer")
       return 

    rental_obj = active_rentals[customer_id]

    ## process return
    print ("Return processing")
    actual_hours = get_rental_period_hours()
    rental_obj.hours = actual_hours

    final_bill = shop.process_return(rental_obj)

    ## update the daily build an remove the rental to return it
    equipment_name = rental_obj.equipment.name
    if equipment_name == "Ski": 
        daily_stats["total skis rented"] += 0
    else: 
        daily_stats["total snowboards rented"] += 0
    daily_stats["total_revenue"] += 0

    del active_rentals[customer_id]


    ## print invoice for return 
    print("\nFinal Invoice:")
    print(f"- Customer: {rental_obj.customer.name} (ID: {rental_obj.customer.customer_id})")
    print(f"- Equipment: {rental_obj.equipment.name}")
    print(f"- Quantity: {rental_obj.quantity}")
    print(f"- Rental hours (actual): {rental_obj.hours}")
    print(f"- Amount due: ${final_bill:.2f}")

    print("Return processed")



#################################
## This calls the main process
##################################


start_application()



## commented out test case below so I know what is going on here. 
#def main():
#    try:
#        print("=== Testing RentalEquipment / Ski / Snowboard ===")
#        skis = ski(10)
#        snowboards = snowboard(8)
#        skis.describe()
#        snowboards.describe()

#        print("\n=== Testing Best Price ===")
#        print(f"Ski best price for 4 hours: ${skis.get_best_price(4):.2f}")  # Should be $50 (daily beats 4x$15=$60)
#        print(f"Snowboard best price for 2 hours: ${snowboards.get_best_price(2):.2f}")  # Should be $20 (hourly)

#        print("\n=== Testing Customer ===")
#        customer1 = customer("Momo", 1)
#        print(f"Customer: {customer1.name} | ID: {customer1.customer_id}")

#        print("\n=== Testing Rental & Discounts ===")
#        rental1 = rental(customer1, skis, 3, 4, "SKIBBP")  # Family + coupon
#        estimate = rental1.calculate_estimate()
#        print(f"Estimate (3 skis, 4hrs, family+coupon): ${estimate:.2f}")

#        print("\n=== Testing RentalShop ===")
#        shop = rental_shop()
#        shop.set_inventory(skis, snowboards)
#        shop.display_available()

#        rental2 = rental(customer1, skis, 2, 8)
#        cost = shop.process_rental(rental2)
#        print(f"Processed rental cost: ${cost:.2f}")
#        shop.display_available()

 #       shop.process_return(rental2)
 #       print("Equipment returned.")
 #       shop.display_available()
 #       shop.display_daily_totals()

#        print("\n=== Testing Inventory Validation ===")
#        too_many = rental(customer1, snowboards, 20, 4)
#        shop.process_rental(too_many)  # Should raise exception

#    except Exception as e:
#        print(f"Exception caught: {e}")

#    finally:
#        print("\nTesting complete.")

#main()