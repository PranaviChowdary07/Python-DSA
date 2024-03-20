""" # optimal solution
def once_appear(nums):
    single = 0
    for num in nums:
        single ^= num
    return single
nums = [1,1,2,2,3,4,4,4,5,5]
Single_number = once_appear(nums)
print("Once apppear number is :",Single_number) """
# Optimal solution to find the number that appears only once
""" def once_appear(nums):
    single = 0
    for num in nums:
        single ^= num
    return single

# Example usage
nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]
single_number = once_appear(nums)
print("Number appearing once is:", single_number) """
# Optimal solution to find the number that appears only once
def once_appear(nums):
    single = 0
    for num in nums:
        single ^= num
    return single

# Example usage
nums = [1, 1, 2, 2, 3, 3,4, 4, 4, 4, 5]
single_number = once_appear(nums)
print("Number appearing once is:", single_number)

