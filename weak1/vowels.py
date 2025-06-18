#counts the number of vowels in a given string using a loop
count=0
msg = "Hello Welcome !!"
vowel = ["a","e","i","o","u"]
for i in vowel:
    count += msg.count(i)
print(count)

