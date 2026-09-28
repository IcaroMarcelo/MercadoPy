from models.product import Product

def register_product(products: list[Product]) -> None:
    name: str = input("Enter the product name: ")
    
    price:float = float(input("Enter the product price: "))

    product = Product(name,price)
        
    products.append(product)

def list_products(products: list[Product]) -> None:
    if not products:
        print("No product registered.")
    else:
        for index,product in enumerate(products,start=1):
            print(f"{index} - {product.name} - ${product.price:.2f}")
            
def buy_product(products:list[Product], cart: dict[Product,int]) -> None:
    
    list_products(products)
    
    choice: int = int(input("Select the product you want to buy: "))
    
    product: Product = products[choice - 1]
    
    quantity: int = int(input("Enter the quantity: "))
    
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity


def view_shopping_cart(cart: dict[Product,int]) -> None:
    
    if not cart:
        print("No products in cart.")
    else:
        for product,quantity in cart.items():
            subtotal = product.price * quantity
            print(f"{product.name}| Quantity: {quantity} | Unit price: ${product.price:.2f} | Subtotal: ${subtotal:.2f}")
            
            
def finish_purchase(cart: dict[Product,int]) -> None:
    if not cart:
        print("No products in cart.")
    else:
        total:float = 0.0
        for product,quantity in cart.items():
            subtotal = product.price * quantity
            total += subtotal

        print(f"Total: ${total:.2f}")

def main() -> None:
    products: list[Product] = []
    cart: dict[Product,int] = {}
    
    while True:
        print("=== MERCADOPY ===")
        print("1 - Register product")
        print("2 - List products")
        print("3 - Buy product")
        print("4 - View shopping cart")
        print("5 - Finish purchase")
        print("6 - Exit")
        choice: int = int(input("Choose an option:"))
        
        if choice == 1:
            register_product(products)
        elif choice == 2:
            list_products(products)
        elif choice == 3:
            buy_product(products,cart)
        elif choice == 4:
            view_shopping_cart(cart)
        elif choice == 5:
            finish_purchase(cart)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()