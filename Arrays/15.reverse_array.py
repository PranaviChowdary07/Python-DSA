def revArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr [start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

arr = [1,2,3,4,5,6,7]
print("Original Arrray:",arr)
#revArrray(arr)
#print(arr)
Reverse_Array = revArray(arr)
print("Reversed Array:",Reverse_Array)
