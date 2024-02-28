from array import array

def find_largest(arr):
    if not arr:
        print("Array is empty")        
        #return None
    max_element = arr[0]
    # for num in arr[1:]: -->also using slice funtion
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element
arr = array('i', [4,14,45,16,7,22,11,56,34])  
largest_element = find_largest(arr)
print("Largest element:",largest_element)

def find_smallest(arr):
    if not arr:
        print("Array is empty")        
        #return None
    min_element = arr[0]
    # for num in arr[1:]: -->also using slice funtion
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element
arr = array('i', [4,14,45,16,2,4,12])  
samllest_element = find_smallest(arr)
print("Smallest element:",samllest_element)