def gcd(a,b):
    while b:
        a , b = b , a % b
    return a

print(gcd(48,60))


# a,b=48,600
# while b:
#     a,b=b,a%b
# print(a)