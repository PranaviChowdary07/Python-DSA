# Function to find the length of the largest subarray with sum K
# Brute code
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
nums = [1, 1, 1, 2, 3, 4]
k = 3
print("Length of the largest subarray with sum", k, "is:", maxSubArrayLen(nums, k))
