
#factorial of a number using a while loop

num=6

print(f"\nFactorial of {num} is",end=" ")
fact=1
while num > 0:
    if(num==1 and num==0):
        print(f"\nfactorial is 1")
        break
    fact = fact * num
    num -= 1
print(fact)

