def linear(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
           return i
    return -1

arr = [3,5,2,50,7,10,6,14]
target = 0
result = linear(arr,target)
if result != -1:
    print(result)
else:
    print("not found")
