n = 7
for i in range(n):
    print(" " * i + " * " * i + " " * (8 * (n-i-1)) + " * " * i)
for i in range(n-2,0,-1):
    print(" " * i + " * " * i + " " * (8 * (n-i-1)) + " * " * i)