from interface import IInventory
from database import ProductModel
from product import Product
# import csv , os

class Inventory(IInventory):
    # FILE_NAME = "inventory.csv"
    def __init__(self, session,role):
        self.session = session
        self.role = role

        # self.products = []
        # self.load_from_file()

    def add_product(self, product):
        existing = self.session.query(ProductModel).filter_by(product_id = product.product_id).first()
        if existing:
            print(f"\nProduct: {product.name} already exists")
        else:
            new_product = ProductModel(
                product_id = product.product_id,
                name = product.name,
                price = product.price,
                quantity = product.quantity
            )
            self.session.add(new_product)
            self.session.commit()
            print(f"\nProduct: {product.name} added successfully")
    
    def update_quantity(self, product_id, quantity_change):
        product = self.session.query(ProductModel).filter_by(product_id = product_id).first()
        if product:
            new_qty = product.quantity + quantity_change
            if new_qty < 0:
                print(f"\nNot enough stock to reduce")
            else:
                product.quantity = new_qty
                self.session.commit()
                print(f"\nQuantity Updated")
        else:
            print(f"\nProduct: {product.name} not found")
    
    def delete_product(self, product_id):
        if self.role != "admin":
            print("Only admin can delete products")
            return
            
        product = self.session.query(ProductModel).filter_by(product_id = product_id).first()
        if product:
            self.session.delete(product)
            self.session.commit()
            print(f"\nProduct: {product.name} deleted")
        else:
            print(f"\nProduct_id: {product_id} not found")
        
    def view_inventory(self):
        products = self.session.query(ProductModel).all()
        if not products:
            print(f"\nProduct not found")
        else:
            for p in products:
                product = Product(p.product_id, p.name, p.price, p.quantity)
                product.display()
        
    def search_product(self, keyword):
        products = self.session.query(ProductModel).all()
        found = False
        for p in products:
            if keyword.lower() in p.name.lower() or keyword == p.product_id:
                product = Product(p.product_id, p.name, p.price, p.quantity)
                product.display()
                found = True
        if not found:
            print(f"\nProduct not found")

    # def save_to_file(self):
    #     with open(self.FILE_NAME, mode='w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(['product_id', 'name', 'category', 'price', 'quantity'])
    #         for p in self.add_products:
    #             writer.writerow([p.product_id, p.name, p.category, p.price, p.quantity])

    # def load_from_file(self):
    #     if not os.path.exists(self.FILE_NAME):
    #         return
    #     with open(self.FILE_NAME, mode='r') as file:
    #         reader = csv.DictReader(file)
    #         for row in reader:
    #             product = Product(
    #                 row['product_id'],
    #                 row['name'],
    #                 row['category'],
    #                 row['price'],
    #                 row['quantity']
    #             )
    #             self.products.append(product)

    # def sort_inventory(self, by):
    #     if by == 'name':
    #         self.products.sort(key=lambda p: p.name.lower())
    #     elif by == 'price':
    #         self.products.sort(key = lambda p: p.price)
    #     elif by == 'quantity':
    #         self.proucts.sort(key = lambda p: p.quantity)
    #     else:
    #         print("Invalid sort key")
    #         return
    #     self.view_inventory()

    # def filter_by_category(self, category):
    #     filtered = [p for p in self.products if p.category.lower()== category.lower()]
    #     if not filtered:
    #         print("No product found in this category")
    #     else:
    #         print(f"\n Products in category: {category} :")
    #         for p in filtered:
    #             p.display()

    

        
        
