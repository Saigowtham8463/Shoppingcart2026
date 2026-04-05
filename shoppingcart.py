"""
Shopping Cart Management System
"""

# ✅ Product Class
class Product:
    def __init__(self, name, price, description, stock_quantity):
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def update_product(self, name, price, description, stock_quantity):
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        print(f"{self.name} updated successfully!")

    def info(self):
        print("\n📦 Product Details")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Description:", self.description)
        print("Stock:", self.stock_quantity)


# ✅ Cart Class
class Cart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        if product.stock_quantity > 0:
            self.products.append(product)
            product.stock_quantity -= 1
            print(f"✅ {product.name} added to cart")
        else:
            print(f"❌ {product.name} is out of stock")

    def remove_from_cart(self, product):
        if product in self.products:
            self.products.remove(product)
            product.stock_quantity += 1
            print(f"🗑 {product.name} removed from cart")
        else:
            print("Product not in cart")

    def show_cart(self):
        print("\n🛒 Your Cart:")
        if not self.products:
            print("Cart is empty")
        else:
            for p in self.products:
                print(f"- {p.name} | ₹{p.price}")

    def total_price(self):
        total = sum(p.price for p in self.products)
        print(f"\n💰 Total Price: ₹{total}")


# ✅ Main Program
def main():
    # Create products
    laptop = Product("Laptop", 50000, "16GB RAM, 512GB SSD", 5)
    phone = Product("Phone", 20000, "8GB RAM, 128GB Storage", 10)
    tablet = Product("Tablet", 15000, "4GB RAM, 64GB Storage", 7)

    products = [laptop, phone, tablet]

    cart = Cart()

    while True:
        print("\n====== 🛍 Shopping Menu ======")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Total Price")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Products:")
            for i, p in enumerate(products):
                print(f"{i+1}. {p.name} | ₹{p.price} | Stock: {p.stock_quantity}")

        elif choice == "2":
            index = int(input("Enter product number to add: ")) - 1
            if 0 <= index < len(products):
                cart.add_to_cart(products[index])
            else:
                print("Invalid choice")

        elif choice == "3":
            index = int(input("Enter product number to remove: ")) - 1
            if 0 <= index < len(products):
                cart.remove_from_cart(products[index])
            else:
                print("Invalid choice")

        elif choice == "4":
            cart.show_cart()

        elif choice == "5":
            cart.total_price()

        elif choice == "6":
            print("Thank you for shopping! 🛒")
            break

        else:
            print("Invalid option, try again!")


# Run the program
if __name__ == "__main__":
    main()