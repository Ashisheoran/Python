#function that accepts any number of arguments and returns their average

def avg(*num):
    n=len(num)
    total = 0
    for i in num:
        total += i
    if n == 0:
        return 0
    return total / n

print(avg(5,6,3,2,0))
