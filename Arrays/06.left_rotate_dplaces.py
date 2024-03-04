from array import array

# Brute code
def left_rotate(arr,k):
    n =len(arr)
    k = k % n
    for _ in range(k):
        temp = arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = temp

arr = [1,2,4,5,6]
k = 2
left_rotate(arr,k)
print(arr)
    
# Optimal
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)


arr = [10,11,12,13,14,15]
k = 4
left_rotate(arr, k)
print("Rotated array:", arr)  
