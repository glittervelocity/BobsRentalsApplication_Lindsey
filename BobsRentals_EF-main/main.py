from Ski import ski
from Snowboard import snowboard
from Customer import customer
from Rental import rental
from RentalShop import rental_shop

def main():
    try:
        print("=== Testing RentalEquipment / Ski / Snowboard ===")
        skis = ski(10)
        snowboards = snowboard(8)
        skis.describe()
        snowboards.describe()

        print("\n=== Testing Best Price ===")
        print(f"Ski best price for 4 hours: ${skis.get_best_price(4):.2f}")  # Should be $50 (daily beats 4x$15=$60)
        print(f"Snowboard best price for 2 hours: ${snowboards.get_best_price(2):.2f}")  # Should be $20 (hourly)

        print("\n=== Testing Customer ===")
        customer1 = customer("Momo", 1)
        print(f"Customer: {customer1.name} | ID: {customer1.customer_id}")

        print("\n=== Testing Rental & Discounts ===")
        rental1 = rental(customer1, skis, 3, 4, "SKIBBP")  # Family + coupon
        estimate = rental1.calculate_estimate()
        print(f"Estimate (3 skis, 4hrs, family+coupon): ${estimate:.2f}")

        print("\n=== Testing RentalShop ===")
        shop = rental_shop()
        shop.set_inventory(skis, snowboards)
        shop.display_available()

        rental2 = rental(customer1, skis, 2, 8)
        cost = shop.process_rental(rental2)
        print(f"Processed rental cost: ${cost:.2f}")
        shop.display_available()

        shop.process_return(rental2)
        print("Equipment returned.")
        shop.display_available()
        shop.display_daily_totals()

        print("\n=== Testing Inventory Validation ===")
        too_many = rental(customer1, snowboards, 20, 4)
        shop.process_rental(too_many)  # Should raise exception

    except Exception as e:
        print(f"Exception caught: {e}")

    finally:
        print("\nTesting complete.")

main()
