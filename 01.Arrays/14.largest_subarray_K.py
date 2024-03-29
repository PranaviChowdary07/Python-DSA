# Function to find the length of the largest subarray with sum K
# Brute code
""" 
def maxSubArrayLen(nums, k):
    max_len = 0
    n = len(nums)
    
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum == k:
                max_len = max(max_len, end - start + 1)
    
    return max_len

# Example usage
nums = [1, 1, 1, 2, 3,3, 4]
k = 5
print("Length of the largest subarray with sum", k, "is:", maxSubArrayLen(nums, k)) """

# Optimal code:
def subArray(nums,k):
    max_len = 0
    sum_index ={0: -1}
    current_sum = 0

    for i ,num in enumerate(nums):
        current_sum += num
        difference = current_sum -k
        if difference in sum_index:
            max_len = max(max_len,i - sum_index[difference])
        # Store the running sum and its corresponding index if not already in sum_to_index
        if current_sum not in sum_index:
            sum_index[current_sum] = i
    return max_len

nums = [1,1,2,3,4,1,1]
k = 5
print("Length of the largest subarray with sum",k,"is :",subArray(nums,k))



        