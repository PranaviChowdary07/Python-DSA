def missing(arr):
    n = len(arr) + 1
    totalsum = n*(n+1)//2   #  n*(n+1)/2 give float value like 2.0
    arr_sum = 0

    for num in arr:
        arr_sum +=  num
    missing_num = totalsum - arr_sum
    return missing_num

arr = [1,2,3,4,5,6,8,9,10]
mising_number = missing(arr)
print("Missing Element :",mising_number)

""" 
OUTPUT:
Missing Element : 
 """