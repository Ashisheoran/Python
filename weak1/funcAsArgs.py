
#Pass a function as an argument to another function and call it.

def cal(add,sub):
    return add,sub
def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
print((cal(sum(5,2),diff(5,2))))

