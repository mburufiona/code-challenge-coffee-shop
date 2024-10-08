# Code Challenge - Coffee Shop

## Overview

This project simulates a simple coffee shop management system using Object-Oriented Programming (OOP) in Python. It includes three main classes:

- Customer
- Coffee
- Order

The relationships between these models are as follows:

- A Customer can have multiple Orders.
- A Coffee can be part of multiple Orders.
- An Order is associated with both a Customer and a Coffee.

## Features

- **Customer Management:** Create and manage customers, track their orders, and identify the customer who has spent the most on a specific coffee.
- **Coffee Management:** Create coffee types, track orders for each coffee, and calculate the number of orders and average price for each coffee.
- **Order Management:** Link customers and coffee with a price, ensuring data integrity and enabling various queries.

## Getting Started

### Requirements

- Python 3.x installed on your machine.
- An IDE or text editor of your choice (such as VS Code, PyCharm, or Sublime Text).

### Installation

1. **Clone the Repository**

```bash
git clone git@github.com:mburufiona/code-challenge-coffee-shop.git
cd code-challenge-coffee-shop
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Create Project Files and Folders

- Organize your project structure as follows:

```css
coffee_shop/
├── ├── coffee.py
│   ├── customer.py
│   └── order.py
└── main.py
├── venv/
├── README.md
```

### Running Tests
To ensure everything is working correctly, you can run the provided test suite. Assuming you have pytest installed, use the following command:
```bash
python3 main.py
```
## Contributing
Feel free to contribute to this project by submitting issues, pull requests, or suggestions. Please follow standard Git workflow practices.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Fiona Nduta](https://github.com/mburufiona)

