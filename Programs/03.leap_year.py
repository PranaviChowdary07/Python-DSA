def is_leap_year(year):
    # Leap years are divisible by 4
    # But not by 100 unless also divisible by 400
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
year = int(input("Enter the year:"))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Another Way
yr = int(input("Enter the year:"))
if yr %4 ==0:
    if yr % 100 ==0:
        if yr % 400 ==0:
            print(yr,"is a leap year")
        else:
            print(yr,"is not a leap year")
    else:
        print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")

