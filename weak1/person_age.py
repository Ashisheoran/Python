# Take an input age and print whether the person is a child, teenager, adult, or senior

age = int(input("Enter age: "))

if(age > 60):print("Senior")
elif(age > 18):print("Adult")
elif(age > 13):print("Teenager")
else:print("Child")

