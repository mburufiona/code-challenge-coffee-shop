class Coffee:
    _all_orders = []  # Initialize an empty list to keep track of all orders

    def __init__(self, name):  # Corrected to use double underscores
        self._set_name(name)
    
    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def orders(self):
        from order import Order  # Delayed import
        return [order for order in Order._all_orders if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)