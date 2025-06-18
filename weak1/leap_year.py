
# Use a nested if condition to determine if a year is a leap year.

year = int(input("Enter Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(year," is leap year")
        else:
            print(year," is not leap year")
    else:
        print(year," is leap year")
else:
    print(year," is not leap year")


