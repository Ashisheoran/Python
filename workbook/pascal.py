n = 5
# c=1
for i in range(n,1,-1):
    for k in range(n-i,0,-1):
        print(end=" ")
    c =1
    for j in range(1,i+1):
        print(c,end=" ")
        c = c*(i-j)//j
        # c = c+1
    print()

triangle = []
for i in range(n):
    row = [1] * (i+1)
    for j in range(1,i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(" " * (n-len(row)),end="") 
    for i in row:
        print(i,end=" ")
    print()
