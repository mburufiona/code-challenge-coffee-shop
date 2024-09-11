 # Represents a coffee drink
class Coffee:
    _all_orders = [] 

    def __init__(self, name):  # Initializes a Coffee object
        self._set_name(name)   # The coffee name
    
    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters.")
        self._name = name

   # property decorator
    @property
    def name(self):
        return self._name  # Returns the name of the coffee
    
    def orders(self):
        from order import Order  # import Order class
        return [order for order in Order._all_orders if order.coffee == self] # Return a list of orders that match this coffee
    
    def customers(self):
        return list(set(order.customer for order in self.orders())) # Returns a list of customers who have ordered this coffee
    
    def num_orders(self):
        return len(self.orders()) # Returns the number of orders for this coffee
    
    def average_price(self):
        orders = self.orders() # Get the list of orders for the coffee
        if not orders:
            return 0
        total_price = sum(order.price for order in orders) # Calculates the total price of all orders
        return total_price / len(orders)  # returns price of coffee