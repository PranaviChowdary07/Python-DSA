from  array import array

def second_largest(arr):
    if len(arr)<2:
        return None
    largest = 0
    second_largest = 0
    for num in arr:
        if num > largest:
             second_largest = largest
             largest = num 
        elif num >second_largest and num != largest:
            second_largest = num
    return second_largest
arr = array('i',[34,23,45,55,12,65])
S_largest = second_largest(arr)
print("second largest element:",S_largest)

""" 
EXPLANATION:
Initialization: largest = second_largest = 0
Iteration 1: num = 34
34 is greater than largest (0), so largest = 34, second_largest = 0.
Iteration 2: num = 23
23 is not greater than largest (34), but it's greater than second_largest (0) and not equal to largest, so second_largest = 23.
Iteration 3: num = 45
45 is greater than largest (34), so largest = 45, second_largest = 34.
Iteration 4: num = 12
12 is not greater than largest (45), but it's greater than second_largest (34) and not equal to largest, so second_largest = 12.
Iteration 5: num = 65
65 is greater than largest (45), so largest = 65, second_largest = 45.
After the iterations, second_largest will hold the value 45, which is the second largest element in the array [34, 23, 45, 12, 65].
 """

def find_second_smallest(arr):
    if len(arr) < 2:
        return None  # Handle edge case when array has less than two elements

    smallest = second_smallest = float('inf')  # Initialize smallest and second_smallest to positive infinity

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

# Example usage:
arr = [3, 6, 1, 8, 4, 9, 2]
second_smallest = find_second_smallest(arr)
print("Second smallest element:", second_smallest)

             

        
