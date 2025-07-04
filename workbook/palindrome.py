text = "madam"
n = len(text)
is_palindrome = True
for i in range(n // 2):
    if text[i] != text[n-i-1]:
        is_palindrome = False

if is_palindrome:
    print(f"The '{text}' is Palindrome")
else:
    print(f"The '{text}' is not Palindrome") 