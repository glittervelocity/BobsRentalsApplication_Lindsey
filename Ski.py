from RentalEquipment import rental_equipment as RE

class ski(RE):

    def __init__(self, starting_inventory):
        RE.__init__(self, "Ski", 15, 50, 200, starting_inventory)

    def describe(self):
        print(f"Skis | Hourly: ${self.hourly_rate} | Daily: ${self.daily_rate} | Weekly: ${self.weekly_rate} | Available: {self.available_inventory}")