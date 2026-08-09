class rental_equipment:

    def __init__(self, name, hourly_rate, daily_rate, weekly_rate, starting_inventory):
        self.name = name
        self.hourly_rate = hourly_rate
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate
        self.starting_inventory = starting_inventory
        self._available_inventory = starting_inventory

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 1:
            raise ValueError("Equipment name must be at least 1 character long.")
        self._name = value

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value < 0:
            raise ValueError(f"Hourly rate cannot be negative. Value was: {value}")
        self._hourly_rate = value

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value < 0:
            raise ValueError(f"Daily rate cannot be negative. Value was: {value}")
        self._daily_rate = value

    @property
    def weekly_rate(self):
        return self._weekly_rate

    @weekly_rate.setter
    def weekly_rate(self, value):
        if value < 0:
            raise ValueError(f"Weekly rate cannot be negative. Value was: {value}")
        self._weekly_rate = value

    @property
    def starting_inventory(self):
        return self._starting_inventory

    @starting_inventory.setter
    def starting_inventory(self, value):
        if value < 0:
            raise ValueError(f"Starting inventory cannot be negative. Value was: {value}")
        self._starting_inventory = value

    @property
    def available_inventory(self):
        return self._available_inventory

    # Reduce inventory when rented
    def rent(self, quantity):
        if quantity > self._available_inventory:
            raise Exception(f"Not enough {self._name}s available. Requested: {quantity}, Available: {self._available_inventory}")
        self._available_inventory -= quantity

    # Restore inventory when returned
    def return_equipment(self, quantity):
        if self._available_inventory + quantity > self._starting_inventory:
            raise Exception(f"Cannot return more {self._name}s than were originally in inventory.")
        self._available_inventory += quantity

    # Determine best price per item for a given number of hours
    def get_best_price(self, hours):
        hourly_total = self._hourly_rate * hours
        daily_total = self._daily_rate * max(1, -(-hours // 8))   # ceiling division for days
        weekly_total = self._weekly_rate * max(1, -(-hours // 56)) # ceiling division for weeks
        return min(hourly_total, daily_total, weekly_total)

    # Subclasses should override this
    def describe(self):
        print(f"{self._name} | Hourly: ${self._hourly_rate} | Daily: ${self._daily_rate} | Weekly: ${self._weekly_rate} | Available: {self._available_inventory}")



