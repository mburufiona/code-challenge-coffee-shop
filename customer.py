class Customer:
    def __init__(self, name):  # Corrected to use double underscores
        self._set_name(name)
    
    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._set_name(new_name)
    
    def orders(self):
        from order import Order  # Delayed import to avoid circular import
        return [order for order in Order._all_orders if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        from coffee import Coffee  # Delayed import
        from order import Order  # Delayed import
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        new_order = Order(self, coffee, price)
        return new_order