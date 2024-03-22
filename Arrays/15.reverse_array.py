def revArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr [start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

#arr =input("Enter the arr values:").split()   --> when array takes from user
#arr = [int (x) for x in arr]
arr = [1,2,3,4,5,6,7]
print("Original Arrray:",arr)
#revArrray(arr)
#print(arr)
Reverse_Array = revArray(arr)
print("Reversed Array:",Reverse_Array)

""" OUTPUT:-

Original Arrray: [1, 2, 3, 4, 5, 6,7]
Reversed Array: [7,6, 5, 4, 3, 2, 1] """
