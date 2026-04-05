"""
This is a python program to create a cart for a shopping website
1. Product managment system: name, price, description, stock_quantity
"""

class Product:
    def __init__(self, name, price, description, stock_quantity):
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    # function to add a product to the cart
    def add_to_cart(self, product):
        self.products.append(product)
        print("Product", self.name, "added to the cart")

    #function to update product details
    def update_product(self, name, price, description, stock_quantity):
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        print("Product", self.name, "updated")

    
    #function to desplay product information
    def info(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Description:", self.description)
        print("Stock Quantity:", self.stock_quantity)
        print("Product", self.name, "info displayed")


# create a product
laptop = Product("Laptop", 1000, "A laptop with 8GB RAM and 256GB storage", 10)
phone = Product("Phone", 500, "A phone with 4GB RAM and 64GB storage", 20)
tablet = Product("Tablet", 300, "A tablet with 2GB RAM and 32GB storage", 30)

# display product information
laptop.info()
print("--------------------------------")
phone.info()
print("--------------------------------")
tablet.info()

#update laptop ram to 16GB

laptop.update_product("Laptop", 1000, "A laptop with 16GB RAM and 256GB storage", 10)

print("--------------------------------")
laptop.info()
print("--------------------------------")

#add tv to the cart
tv = Product("TV", 25000, "A tv with 4K resolution and 55 inch screen", 10)
print("--------------------------------")
tv.info()

print("--------------------------------")
tv.update_product("tv", 9999, "A tv with 8K resolution and 75 inch screen",80)
print("--------------------------------")
tv.info()