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
def left_rotate(arr,k)