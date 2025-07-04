string = input("Enter a String: ")
countDigit = 0
countAlpha = 0
countChar = 0
for char in string:
    if char.isdigit():
        countDigit += 1
    elif char.isalpha():
        countAlpha += 1
    else:
        countChar += 1
print(f"Digit are {countDigit}")
print(f"Alphabets are {countAlpha}")
print(f"Special Characters are {countChar}")