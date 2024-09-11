from customer import Customer
from coffee import Coffee
from order import Order

# Create instances of Coffee
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create instances of Customer
customer1 = Customer("Fiona")
customer2 = Customer("mburu")

# Customers create orders
order1 = customer1.create_order(coffee1, 3.5)
order2 = customer2.create_order(coffee1, 4.0)
order3 = customer1.create_order(coffee2, 5.0)

# Access coffee information
print(f"Number of orders for {coffee1.name}: {coffee1.num_orders()}")
print(f"Average price for {coffee1.name}: {coffee1.average_price()}")

# Access customer information
print(f"{customer1.name} has ordered the following coffees: {[coffee.name for coffee in customer1.coffees()]}")
print(f"Total number of orders for {customer1.name}: {len(customer1.orders())}")

# Access order details
print(f"Order 1 details - Customer: {order1.customer.name}, Coffee: {order1.coffee.name}, Price: {order1.price}")
print(f"Order 2 details - Customer: {order2.customer.name}, Coffee: {order2.coffee.name}, Price: {order2.price}")
print(f"Order 3 details - Customer: {order3.customer.name}, Coffee: {order3.coffee.name}, Price: {order3.price}")