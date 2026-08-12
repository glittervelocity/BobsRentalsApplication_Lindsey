from RentalEquipment import rental_equipment as RE

class snowboard(RE):

    def __init__(self, starting_inventory):
        RE.__init__(self, "Snowboard", 10, 40, 160, starting_inventory)

    def describe(self):
        print(f"Snowboards | Hourly: ${self.hourly_rate} | Daily: ${self.daily_rate} | Weekly: ${self.weekly_rate} | Available: {self.available_inventory}")