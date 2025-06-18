# function with a nested inner function and use `nonlocal` to modify its variable

def outer():
    num = 32
    print(id(num))
    def inner():
        nonlocal num
        num = 62
        print(id(num))
        print(num)
    inner()


outer()