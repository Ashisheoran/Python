num = int(input("Enter Number: "))      #153
power = len(str(num))
sum = 0
temp = num                              #153
while temp: 
    digit = temp % 10                   # 3 , 5 , 1
    sum += digit ** power               # 3^3 , 3^3 + 5^3 + 1^3
    temp //= 10                         # 15 , 1 , 0

if sum == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not Armstrong Number")
