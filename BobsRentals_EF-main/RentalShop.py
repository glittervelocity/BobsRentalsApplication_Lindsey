class rental_shop:

    def __init__(self):
        self._ski_inventory = None
        self._snowboard_inventory = None
        self._daily_skis_rented = 0
        self._daily_snowboards_rented = 0
        self._daily_revenue = 0.0

    # Set starting inventory for each equipment type
    def set_inventory(self, ski_equipment, snowboard_equipment):
        self._ski_inventory = ski_equipment
        self._snowboard_inventory = snowboard_equipment

    def display_available(self):
        print("--- Available Equipment ---")
        if self._ski_inventory:
            self._ski_inventory.describe()
        if self._snowboard_inventory:
            self._snowboard_inventory.describe()

    # Process a rental — reduce inventory and track daily totals
    def process_rental(self, rental):
        rental.equipment.rent(rental.quantity)
        cost = rental.calculate_estimate()

        if rental.equipment.name == "Ski":
            self._daily_skis_rented += rental.quantity
        else:
            self._daily_snowboards_rented += rental.quantity

        self._daily_revenue += cost
        return cost

    # Process a return — restore inventory
    def process_return(self, rental):
        rental.equipment.return_equipment(rental.quantity)
        return rental.calculate_final_bill()

    def display_daily_totals(self):
        print("--- Daily Totals ---")
        print(f"Skis rented today:       {self._daily_skis_rented}")
        print(f"Snowboards rented today: {self._daily_snowboards_rented}")
        print(f"Total revenue today:     ${self._daily_revenue:.2f}")