#check first is greater than, less than, or equal to the second.

num1=int(input('Enter First Number:'))
num2=int(input('Enter Second Number:'))

if(num1>num2):
    print(f'{num1} is greater then {num2}')
elif(num1<num2):
    print(f'{num1} is less then {num2}')
else:
    print(f'{num1} is equal to 5{num2}')




#Check if the number 4 is both greater than 2 and less than 10 using logical operators.

num=4
if(num > 2 and num < 10):
    print(f"\nThe number {num} is greater than 2 and less than 10")
else:
    print('\nCondition is not satisfied')