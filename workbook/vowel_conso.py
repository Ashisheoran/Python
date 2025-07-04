char =  input("Enter a character: ").lower()

if char in "aeiou":
    print("The character is vowel")
elif char.isalpha():
    print("The character is consonant")
else:
    print("Enter a valid character")