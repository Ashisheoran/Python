class Product:
    '''Represents a product available for sale'''
    def __init__(self,name,price,stock,product_id) -> None:
        self.name = name
        self.price = price
        self.stock = stock
        self.product_id = product_id
    
    def display_info(self):
        '''display product details'''
        print(f"Id: {self.product_id:<4} | Name: {self.name:<10} | Price: {self.price:<8.2f} | Stock: {self.stock}")
    
    def update_stock(self,quantity):
        '''To adjust stock after a purchase or return'''
        self.stock += quantity

class ShoppingCart:
    '''Manage Items which user want to buy'''
    def __init__(self) -> None:
        # item :{product_id : {'product' : Product_obj , 'quantity' : int}}
        self.items = {}
    def add_item(self,product,quantity):
        '''Adds products to cart and manage availiblity'''
        if product.stock < quantity:
            print(f"Sorry... only {product.stock} units of {product.name} available ")
            return False
        if product.product_id in self.items:
            #checking adding more item exceed the available stock
            print(product.product_id)
            if product.stock < ((self.items[product.product_id]['quantity']) + quantity):
                print(f"Adding {quantity} more units would exceed stock Only {product.stock - self.items[product.product_id]['quantity']} More Available in stock.")
                return False
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product':product , 'quantity':quantity }
        print(f"{quantity} {product.name} added to cart")
        return True

t_shirt = Product('t_shirt',500,25,2)
quantity = 20

shoppingCart = ShoppingCart() 

shoppingCart.add_item(t_shirt,quantity)
Product.display_info(t_shirt)
Product.display_info(t_shirt)
