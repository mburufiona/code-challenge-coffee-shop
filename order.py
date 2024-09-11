class Order:
    _all_orders = []  # Class-level list to keep track of all orders
    
    def __init__(self, customer, coffee, price):  # Corrected to use double underscores
        self._set_customer(customer)
        self._set_coffee(coffee)
        self._set_price(price)
        Order._all_orders.append(self)  # Append order to class-level list
    
    def _set_customer(self, customer):
        from customer import Customer  # Delayed import
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer.")
        self._customer = customer
    
    def _set_coffee(self, coffee):
        from coffee import Coffee  # Delayed import
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        self._coffee = coffee
    
    def _set_price(self, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee