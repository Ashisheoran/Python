# Main Function
def calculator(*oper):
    oper_name = [add]
    for i in oper:
        result = "".join(map(str,i))
        print(result)
    return i


# Operation on numbers
def add(*num):
    if len(num) < 2:
        return "Need two numbers for addition"
    total = 0
    for i in num:
        total += i
    return f"Sum is {total}"

def sub(*num):
    if len(num) < 2:
        return "Need two numbers for subtraction"
    result = num[0]
    for i in num[1:]:
        result -= i
    return f"Subtraction is {result}"

def product(*num):
    if len(num) < 2:
        return "Need two numbers for product"
    result = 1
    for i in num:
        result *= i
    return f"Product is {result}"

def division(*num):
    if len(num) < 2:
       return "Need two numbers for division"
    result = num[0]
    for i in num[1:]:
        if i == 0:
            return "Error : Division by zero"
        result /= i
    return f"Division is {result}"


def remainder(*num):
    if len(num) < 2:
       return "Need two numbers for division"
    result = num[0]
    for i in num[1:]:
        result %= i
    return f"Remainder is {result}"


def quotient(*num):
    if len(num) < 2:
       return "Need two numbers for division"
    result = num[0]
    for i in num[1:]:
        result //= i
    return f"Quotient is {result}"



#Call Function Calculator and give values

calculator(add(5,3,6,1),sub(5,3,6,3),product(3,6,4,6,1),division(53,6,3),remainder(53,6,3),quotient(53,6,3))



