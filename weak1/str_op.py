#strips white space and converts a string to uppercase

str1 = "   Ashu      "
print(str1.strip().upper())


#Take a string input and split it by commas and join them using semicolons

str2 =input("Enter String : ")
print(":".join(str2.split(",")))


#Check if a string ends with '.com' and starts with 'www'

str3 = input("Enter string for site ")
print(str3.startswith("www") and str3.endswith(".com"))



#Create a list and demonstrate append, pop, and indexing operations

lst = [3,4,2,8,"Ram","B",9]
print(lst)
lst.append("Sita")
print(lst)
lst.pop(5)
print(lst)
print(lst[6])

