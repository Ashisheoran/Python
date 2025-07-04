num = int(input('enter Number: '))         #765

original = num 
rev_num = 0

while num > 0:
    digit = num % 10                # 5 , 6 , 7
    rev_num = rev_num * 10 + digit  # 5 , 56 , 567
    num //= 10                      # 76 , 7 , 0

print(f"Reverse Number is {rev_num}")                      # 567