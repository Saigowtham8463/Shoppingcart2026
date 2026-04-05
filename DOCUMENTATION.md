Shopping Cart Management System – Project Documentation
1. Introduction

The Shopping Cart Management System is a Python-based console application designed to simulate basic functionalities of an e-commerce platform. The project focuses on implementing core concepts of Object-Oriented Programming (OOP) such as classes, objects, encapsulation, and modular design.

2. Objective
To develop a simple shopping cart system using Python
To understand and apply OOP concepts
To simulate real-world e-commerce operations like product management and cart handling

3. Technologies Used
Programming Language: Python
Concepts: OOP (Classes, Objects, Methods)
Platform: Command Line Interface (CLI)

4. System Design
   
🔹 4.1 Product Class

Handles product-related operations:

Product name
Price
Description
Stock quantity
Update product details
Display product information

🔹 4.2 Cart Class

Handles cart operations:

Add products to cart
Store multiple products
Display cart items


5. Functional Requirements
Add new products
Update existing product details
Display product information
Add products to cart
View cart items

6. Working Flow
Create product objects (Laptop, Phone, etc.)
Display product details
Update product information if needed
Create a cart object
Add products to the cart
Display cart contents

7. Code Implementation (Summary)
Defined Product class with attributes and methods
Defined Cart class to manage cart items
Used lists to store products dynamically
Implemented functions for updating and displaying data

8. Sample Output
Product: Laptop
Price: 1000
Description: 16GB RAM, 256GB storage
Stock Quantity: 10

Laptop added to cart

Cart Items:
- Laptop | Price: 1000
- Phone | Price: 500
  
9. Features
Simple and user-friendly design
Modular code structure
Easy to extend and modify
Demonstrates real-world application logic

10. Limitations
No graphical user interface (GUI)
No database integration
Limited to console-based interaction

11. Future Enhancements
Add GUI using Tkinter
Integrate database (MySQL / SQLite)
Develop web version using Flask/Django
Add payment and billing system
Implement user authentication

12. Conclusion

This project successfully demonstrates the implementation of a basic shopping cart system using Python and OOP principles. It provides a strong foundation for building advanced e-commerce applications.
