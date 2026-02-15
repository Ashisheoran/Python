from interface import IProduct

class Product(IProduct):
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name 
        # self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        alert = "LOW STOCK! " if self.quantity < 5 else ""
        print(f"ID: {self.product_id:<6} | Name: {self.name:<10} | Price: ₹{self.price:<10} | quantity: {self.quantity} {alert}")
    
        