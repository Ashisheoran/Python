#lambda function to calculate the square of a number and use it in a loop

square = lambda num: num**2

for i in range(1,10):
    print(f"Square of numbers {i} is {square(i)}")



#Store a lambda function inside a dictionary and call it

operation={
    "square" : lambda num : num ** 2,
    "cube" : lambda num : num**3
}
num=4

print(f"\nsquare of number {num} is {operation['square'](num)}")
print(f"cube of number {num} is {operation['cube'](num)}")


