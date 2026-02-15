from abc import ABC,abstractmethod

class IProduct(ABC):
    @abstractmethod
    def display(self):
        pass

class IInventory(ABC):
    @abstractmethod
    def add_product(self,product):   pass
    
    @abstractmethod
    def delete_product(self,product_id):   pass

    @abstractmethod
    def update_quantity(self,product_id, quantity_change) :  pass

    @abstractmethod
    def view_inventory(self):  pass

    @abstractmethod
    def search_product(self,keyword):  pass
    
    # @abstractmethod
    # def save_to_file(self):  pass

    # @abstractmethod
    # def sort_inventory(self,by):  pass

    # @abstractmethod 
    # def filter_by_category(self,category):  pass
    