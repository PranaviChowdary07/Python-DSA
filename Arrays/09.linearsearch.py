def linear(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
           return i
    return -1

arr = [3,5,2,5,7]
target = 2
result = linear(arr,target)
if result != -1:
    print(result)
else:
    print("not found")
