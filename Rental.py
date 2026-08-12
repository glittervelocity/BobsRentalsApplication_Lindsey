class rental:

    def __init__(self, customer, equipment, quantity, hours, coupon_code=""):
        self.customer = customer
        self.equipment = equipment
        self.quantity = quantity
        self.hours = hours
        self.coupon_code = coupon_code

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError(f"Rental quantity must be at least 1. Value was: {value}")
        if value > 5:
            raise ValueError(f"Rental quantity cannot exceed 5 items. Value was: {value}")
        self._quantity = value

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if value <= 0:
            raise ValueError(f"Rental hours must be greater than 0. Value was: {value}")
        self._hours = value

    # Calculate estimated cost before renting
    def calculate_estimate(self):
        base_cost = self.equipment.get_best_price(self._hours) * self._quantity
        base_cost = self._apply_discounts(base_cost)
        return base_cost

    # Calculate final bill on return — same logic, just named separately
    def calculate_final_bill(self):
        return self.calculate_estimate()

    # Apply family discount (3-5 items = 25% off) then coupon (ends in BBP = 10% off)
    def _apply_discounts(self, cost):
        if self._quantity >= 3:
            cost = cost * 0.75
            print(f"Family discount applied: 25% off")
        if self.coupon_code.upper().endswith("BBP"):
            cost = cost * 0.90
            print(f"Coupon discount applied: 10% off")
        return cost