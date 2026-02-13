from abc import ABC,abstractmethod
from datetime import datetime

class Library:
    def __init__(self):
        self.items = []
        self.members = [] 

       
    def display_items(self):
        for item in self.items:
            # print(self.item)
            print(item)
        else:
            print("No item available in the library")

    def display_members(self):
        for member in self.members:
            print(member)
        else:
            print("No Member Available in Library")

class Members(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def id(self):
        pass
        
class NewMember(Members):
    def __init__(self,name,id) -> None:
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id 
    
       
    def __str__(self) -> str:
        return f"\nMember name : {self.__name}\nMember ID   : {self.__id}"

class StaffMember(NewMember):
    def __init__(self, name, id, role="librarian", type = "Staff Member") -> None:
        super().__init__(name,id)
        self.__role = role
        self.type = type
    
    def __str__(self) -> str:
        return super().__str__() +f"\nType        : {self.type}\nRole        : {self.__role}"

class PrimiumMember(NewMember):
    def __init__(self, name, id, type = "Primium Member", perks=None) -> None:
        super().__init__(name, id)
        perks = ['Priority Booking','Free E-Book']
        self.perks = perks
        self.type = type
    def __str__(self) -> str:
        return super().__str__() + f"\nType        : {self.type} \nPerks       : {', '.join(self.perks)}"
    
class RegularMember(NewMember):
    def __init__(self, name, id, type = "Regular Member") -> None:
        super().__init__(name, id)
        self.type = type
    
    def __str__(self) -> str:
        return super().__str__() + f"\nType        : {self.type}"

class ManageMember:
   
    def add_members(self,member:Members,lib:Library):
        if member is None:   return "No member Provided"
        if lib is None:    return "No Library provided"
        lib.members.append(member)
        return f"\n{member.type} added Successfully {member}"
    
    def remove_members(sefl,member:Members,lib:Library):
        if member is None:   return "No member Provided"
        if lib is None:    return "No Library provided"
        if member in lib.members:
            lib.members.remove(member)
            return f"\n{member.name} removed Succssfully"
        else:
            return f"\n{member.name} is not in Library"
        
class LibraryItem(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def creator(self):
        pass
    
    @property
    @abstractmethod
    def copies(self):
        pass
    
    def is_available(self):
        if self.copies > 0:
            return True
        else:
            return False
        
class Book(LibraryItem):
    def __init__(self,title,creator,copies):
        self.__title = title
        self.__creator = creator
        self.__copies = copies
    @property   
    def title(self):
        return self.__title 
    
    @property
    def creator(self):
        return self.__creator
    
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def copies(self,value):
        self.__copies = value

    def __str__(self):
        return f"\nBook   : {self.__title}\nAuthor : {self.__creator} \ncopies : {self.__copies}"

class NewsPaper(LibraryItem):
    def __init__(self,title,creator,copies):
        self.__title = title
        self.__publisher = creator
        self.__copies = copies
    @property   
    def title(self):
        return self.__title 
    
    @property
    def creator(self):
        return self.__publisher
    
    # @property
    # def date()
    
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def copies(self,value):
        self.__copies = value

    def __str__(self):
        return f"\nNewsPaper : {self.__title}\nPublisher : {self.__publisher} \ncopies    : {self.__copies}"

class ManageItem:
    def add_item(self,item:LibraryItem,lib:Library):
        if item is None:    return "No item selected"
        if lib is None:    return "No library selected"
        
        lib.items.append(item)
        return f"\n{item.title} added successfully"

    def remove_item(self, item: LibraryItem,lib:Library):
        if item is None:     return "No item selected"
        if lib is None:     return "No library selected"
        if item in lib.items:
            lib.items.remove(item)
            return f"{item.title} removed successfully"
        else:
            return f"{item.title} is not in Library"
        
    def borrow_item(self,item:LibraryItem,lib:Library):
        if item is None:     return "No item selected"
        if lib is None:     return "No Library selected"
        if item in lib.items:
            if item.is_available():
                item.copies-=1
                return f"{item.title} borrowed successfully"
            else:
                return f"{item.title} currently not available"
        else:
            return f"{item.title} is not in library"
    
    def return_item(self,item:LibraryItem,lib:Library):
        if item is None:    return "No item selected"
        if lib is None:    return "No Library selected"
        if item in lib.items:
            item.copies += 1
            return f"{item.title} returned successfully"
        else:
            return f"{item.title} is not of this library"

library = Library()
manager = ManageMember()
librarian = ManageItem()

while True:
    print("\nLIBRARY MENU")
    
    print("\n1. Register Member\n2. View Members \n3. View Items\n4. Add Item\n5. Remove Item\n6. Borrow Item\n7. Return Item\n8. Exit")
    choice =input("Enter Your Choice: ")
    match choice:
        case '1':
            name = input("Enter Member Name: ")
            id = input("Enter Member Id: ")
            member_type = input("Enter Member Type (Staff/Primium/Regular)")
          
            if member_type == "Staff":
                member = StaffMember(name,id)
            elif member_type == "Primium":
                member = PrimiumMember(name,id)
            elif member_type == "Regular":
                member = RegularMember(name,id)
            else:
                print("Invalid Member Type")

            print(manager.add_members(member,library))
        
        case '2':
            library.display_members()
        
        case '3':
            library.display_items()

        case '4':
           member_type = input("Enter Member Type (Staff/Primium/Regular): ")
           if member_type == "Staff":
               item = input("Enter Item to add (Book/Newspaper): ")
               if item == "Book":
                title = input("Book Title: ")
                author = input("Book Author: ")
                copies = input("Enter Copies: ")

                book = Book(title,author,copies)
                librarian.add_item(book,library)
                
               if item == "Newspaper":
                    title = input("Newspaper Title: ")
                    publisher = input("Newspaper publisher: ")
                    copies = input("Enter Copies: ") 
                    newspaper = NewsPaper(title,publisher,copies)
                    librarian.add_item(newspaper,library,member)
           else:
               print("Only Staff Member add items")

        case '5':
            member_type = input("Enter Member Type (Staff/Primium/Regular): ")
            if member_type == "Staff":
                item = input("Enter Item to add (Book/Newspaper): ")
                if item == "Book":
                    title= input("Enter Book Name: ")
                    author = input("Enter Book Author: ")
                    copies = input("Enter Copies: ")
                    book = Book(title,author,copies)
                    librarian.remove_item(book,library)
                    
                if item == "Newspaper":
                    title = input("Enter Newspaper Name: ")
                    publisher = input("Enter Newspaper Author: ")
                    copies = input("Enter Copies: ")
                    newspaper = NewMember(title,author,copies)
                    librarian.remove_item(newspaper,library)
        
        case '6':
                item = input("Enter Item to add (Book/Newspaper): ")
                if item == "Book":
                    title= input("Enter Book Name: ")
                    author = input("Enter Book Author: ")
                    copies = input("Enter Copies: ")
                    book = Book(title,author,copies)
                    librarian.borrow_item(book,library)
                    
                if item == "Newspaper":
                    title = input("Enter Newspaper Name: ")
                    publisher = input("Enter Newspaper Author: ")
                    copies = input("Enter Copies: ")
                    newspaper = NewMember(title,author,copies)
                    librarian.borrow_item(newspaper,library)

        case '7':
            item = input("Enter Item to add (Book/Newspaper): ")
            if item == "Book":
                title= input("Enter Book Name: ")
                author = input("Enter Book Author: ")
                copies = input("Enter Copies: ")
                book = Book(title,author,copies)
                librarian.return_item(book,library)
                
            if item == "Newspaper":
                title = input("Enter Newspaper Name: ")
                publisher = input("Enter Newspaper Author: ")
                copies = input("Enter Copies: ")
                newspaper = NewMember(title,author,copies)
                librarian.return_item(newspaper,library)

        case '8':
            break
