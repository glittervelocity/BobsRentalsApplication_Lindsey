class customer:

    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 1:
            raise ValueError("Customer name must be at least 1 character long.")
        self._name = value

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        if value <= 0:
            raise ValueError(f"Customer ID must be greater than 0. Value was: {value}")
        self._customer_id = value