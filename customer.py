class Customer:

    # Initialize a new customer instance with a given name
    def __init__(self, name):  
        self._set_name(name)
    
    def _set_name(self, name):
        if not isinstance(name, str): # set the customer's name
            raise TypeError("Name must be a string.")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = name
    
    @property
    def name(self):
        return self._name # gets customer's name
    
    @name.setter
    def name(self, new_name):
        self._set_name(new_name) # sets customer's name which calls the set_name method
    
    def orders(self):
        from order import Order  
        return [order for order in Order._all_orders if order.customer == self] # Returns a list of orders associated with the customer
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders())) # Returns a list of unique coffees ordered by the customer
    
    # Create a new order for this customer with the given coffee and price
    def create_order(self, coffee, price): 
        from coffee import Coffee  
        from order import Order  
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        new_order = Order(self, coffee, price)
        return new_order