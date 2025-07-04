sum = 0
for i in range(1,11):
    num = int(input(f"Enter number {i} : "))
    sum += num
avg = sum / i
print(f"The Sum of number is {sum} and total numbers are {i} ... So average is {avg}")