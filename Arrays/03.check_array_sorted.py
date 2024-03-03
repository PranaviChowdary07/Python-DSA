def isSorted(t):
    n = len(t)
    for i in range(1,n):
        if t[i]<t[i-1]:
            return False
    return True
n = int(input("Enter n:"))
a = []
print("Enter the values one by one:")
for  i in  range(0,n):       # this line only for enter the list
    a.append(int(input()))
if isSorted(a):
    print("Array is Sorted")
else:
    print("Array is not Sorted")