       # Left Rotate the Array by One Place
from array import array

def left_rotate(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
   
    

arr= [1,2,3,4,5,6]
left_rotate(arr)
print(arr)

