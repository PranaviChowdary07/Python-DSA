
def right_rotate(arr, d):
    n = len(arr)
    for _ in range(d):
        temp = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
    return arr

# Example usage:
arr = [6,7,8,9,10]
d = 2
rotated_arr = right_rotate(arr, d)
print("Right Rotate Array:",rotated_arr)

# optimal
def rightRotate(arr, d):
    n = len(arr)
    d = d % n
    arr[:] = arr[-d:] + arr[:-d]    
    return arr
arr = [1,2,3,4,5]
d = 2
rotated_arr = rightRotate(arr, d)
print("Right Rotate Array:",rotated_arr) 

""" 
 arr[:] = arr[-d:] + arr[:-d]
 arr[-d:] -->it takes last elements they are d values
 arr[:-d] --> it takes remaining elements
  explanation how it works:

Let's break down the line arr[:] = arr[-d:] + arr[:-d] with an example to understand how it works:

Suppose we have an array arr = [1, 2, 3, 4, 5] and we want to right rotate it by d = 2 places.

Calculate effective rotation amount:

n = len(arr) is the length of the array, which is 5.
d = d % n, so d = 2 % 5, which is 2.
Array slicing:

arr[-d:]: This selects the last 2 elements of the array, which are [4, 5].
arr[:-d]: This selects all elements of the array except the last 2 elements, which are [1, 2, 3].
Concatenating these two parts gives [4, 5] + [1, 2, 3], resulting in [4, 5, 1, 2, 3].
Updating the original array:

arr[:] = [4, 5, 1, 2, 3]: This updates the entire original array arr with the result of concatenation.
After executing arr[:] = arr[-d:] + arr[:-d], the original array arr becomes [4, 5, 1, 2, 3], which is the result of right rotating the original array [1, 2, 3, 4, 5] by 2 places.







    """

