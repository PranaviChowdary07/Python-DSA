# Remove duplicates from sorted array
# set not allow duplicate values
from  array import array

def remove_duplicates(nums):
    if not nums:
        return 0
    unique_index =0
    
    for i in range (1,len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index+=1
            nums[unique_index] = nums[i]
    return unique_index+1
sortedArray = [1,1,1,2,2,3,3,3,4,4] 
s = remove_duplicates(sortedArray)
print(sortedArray[:s])

""" 
OUTPUT:
[1, 2, 3, 4]
 """
"""
 without def function:
  
num_list = [1,2,3,4,3,5,6,2]
new_list = []
for num in num_list:
  if (num not in new_list):
     new_list.append(num)
   
print("List after remove duplicate:",new_list)
 """

def remove_duplicates(num_list):
   
    new_list = []
    for num in num_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

num_list = [1, 2, 3, 4, 3, 5, 6, 2]
unique_list = remove_duplicates(num_list)
print("List after removing duplicates:", unique_list)

