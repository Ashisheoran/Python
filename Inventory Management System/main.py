from database import Session, create_tables
from inventory import Inventory
from product import Product
from auth import login , register
 

class InventoryApp:
    def __init__(self,session,user):
        self.session = session
        self.user = user
        self.inventory = Inventory(session, user.role)

    
    def run(self):
        while True:
            print("\n Inventory Management Menu: ")
            print("1. Add New Product")
            print("2. Update Product Quantity")
            print("3. Delete Product")
            print("4. View Inventory")
            print("5. Search Inventory")
            print("6. Exit")

            choice = input("Choose and option (1-6): ")

            match choice:
                case '1':
                    pid = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    try:
                        price = float(input("Enter Product Price: ₹"))
                        qty = int(input("Enter Quantity: "))
                        product = Product(pid, name, price, qty)
                        self.inventory.add_product(product)
                    except ValueError:
                        print("Invalid input for price or quantity")

                
                case '2':
                    pid = input("Enter Product ID: ")
                    try:
                        qty_change =  int(input("Enter quantity to add/reduce (use - for reduce): "))
                        self.inventory.update_quantity(pid,qty_change)
                    except ValueError:
                        print("Invalid Quantity")

                case '3':
                    p_id = input("Enter Product ID to delete: ")
                    self.inventory.delete_product(p_id)
                
                case '4':
                    self.inventory.view_inventory()
                
                case '5':
                    keyword = input("Enter Product Name of ID to search: ")
                    self.inventory.search_product(keyword)

                case '6': 
                    print("Exiting... Thank You!")
                    break
                    

                case _:
                    print("Invalid option. Please select between 1-6")

                
                
if __name__ == "__main__":
    create_tables()
    session = Session()
    print("Welcome to Inventory System")
    while True:
        print("\n1. Login \n2. Register \n3. Exit")
        choice = input("Choose: ")
        match choice:
            case '1':
                user = login(session)
                if user:
                    app = InventoryApp(session,user)
                    app.run()
                    break
            case '2':
                register(session)
            
            case '3':
                print("Exiting... Bye!")
                break
            
            case _:
                print("Invalid option. Please select between 1-3")

