# Class list to store all orders
class Order:
    _all_orders = []  
    
# Initialize an order instance with customer, coffee and price
    def __init__(self, customer, coffee, price):  
        self._set_customer(customer)
        self._set_coffee(coffee)
        self._set_price(price)
        Order._all_orders.append(self)  # adds the new order to the class list
    
    def _set_customer(self, customer):
        from customer import Customer  #imports customer class
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer.")
        self._customer = customer # set customer attribute
    
    def _set_coffee(self, coffee):
        from coffee import Coffee  # import coffee class
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        self._coffee = coffee # set the coffee attribute
    
    def _set_price(self, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = price # set the price attribute
    
    # property to access the price attribute
    @property
    def price(self):
        return self._price
    
    # property to access the customer attribute
    @property
    def customer(self):
        return self._customer
    
 # property to access the coffee attribute
    @property
    def coffee(self):
        return self._coffee