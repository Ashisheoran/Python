#print all numbers from 1 to 20, except multiples of 5

for num in range(1,20):
    if(num%5==0):
        continue
    print(num,end=" ")

