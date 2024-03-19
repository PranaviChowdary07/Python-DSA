def max_consecutive_zeros_ones(arr):
    max_count = 0
    count = 0

    for num in arr:
        if num == 1:     # num ==0 it counts 0,nums ==1,it counts 1's
            count += 1

        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)  
    return max_count
array = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1,1,1, 1]

print("Max consecutive nums in array :",max_consecutive_zeros_ones(array))
