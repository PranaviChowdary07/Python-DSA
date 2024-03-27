def leapyear(n):
    for i in n:
        if n %4 ==0:
            print("leap year")
        else:
            print("no")
n = int(input("Enter a year: "))
leap = leapyear(n)
print(leap)
