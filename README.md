# MercadoPy

MercadoPy is a simple marketplace application developed in Python as part of a final course project.

The application runs in the terminal and allows users to register products, list available products, add products to a shopping cart, view the cart and calculate the final purchase total.

## Features

- Register products
- List registered products
- Select products to buy
- Add quantities to the shopping cart
- Update the quantity if the same product is added again
- View shopping cart
- Calculate subtotal for each product
- Calculate the final purchase total
- Exit the application through the main menu

## Project Structure

```text
MercadoPy/
├── models/
│   ├── __init__.py
│   └── product.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── market.py
├── teste.py
├── README.md
├── .gitignore
└── .gitattributes
```

## Main Class

### Product

The `Product` class represents a product available in the marketplace.

Each product stores:

- Name
- Price

The class uses encapsulation and properties to provide controlled access to its attributes.

## Product Registration

The application allows users to register new products by entering:

- Product name
- Product price

Each product is stored in a list containing all registered products.

## Shopping Cart

The shopping cart is represented by a dictionary:

```python
dict[Product, int]
```

Where:

```text
Product → quantity
```

If the selected product is already in the cart, the quantity is increased instead of creating another entry.

## Purchase Flow

The application follows this general flow:

```text
Start application
↓
Register products
↓
List available products
↓
Select a product
↓
Enter quantity
↓
Add product to cart
↓
View shopping cart
↓
Calculate purchase total
```

## Main Menu

The application provides the following options:

```text
=== MERCADOPY ===
1 - Register product
2 - List products
3 - Buy product
4 - View shopping cart
5 - Finish purchase
6 - Exit
```

## Purchase Calculation

For each product in the shopping cart, the application calculates:

```text
subtotal = product price × quantity
```

The final purchase total is calculated by adding all subtotals.

## Concepts Practiced

This project was developed to practice:

- Python
- Object-Oriented Programming
- Classes and objects
- Encapsulation
- Properties
- Type Hinting
- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- Shopping cart logic
- Modules and packages
- Code organization

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd MercadoPy
```

Run the application:

```bash
python market.py
```

## Project Status

Completed and functional.
