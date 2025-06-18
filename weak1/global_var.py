
#function that uses a global variable and modifies it

count = 0
print("count outside the function before increment is ",count)
def increment():
    global count
    count += 1
    print("Count inside the function is ",count)
increment()
print("count outside the function after increment is ",count)

