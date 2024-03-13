def missing(arr):
    n = len(arr) + 1
    totalsum = n*(n+1)//2   #  n*(n+1)/2 give float value like 2.0
    arr_sum = 0

    for num in arr:
        arr_sum +=  num
    missing_num = totalsum - arr_sum
    return missing_num

arr = [1,3,4,5,6,7,8,9,10]
mising_number = missing(arr)
print("Missing Element :",mising_number)

""" 
OUTPUT:
Missing Element : 2

EXAPLANATION:
 n  = 5
* The given array is [1,3,4, 5].
* The length of the array is 4, so the expected length (if no number is missing) is 5.
* The expected sum of all numbers from 1 to 5 is calculated as (5 * (5 + 1)) / 2 = 15.
* The actual sum of the numbers in the array [1, 2, 3, 5] is 1 + 3 + 4 + 5 = 13.
* The missing number is calculated as expected_sum - actual_sum = 15 - 13 = 2.
* Therefore, the missing number in the array is 2.
* The code prints: The missing number is: 2

 """