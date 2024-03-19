    # Union of two sorted arrays.
def union_of_sorted_arrays(arr1, arr2):
    union_set = set()
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union_set.add(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union_set.add(arr2[j])
            j += 1
        else:
            union_set.add(arr1[i])
            i += 1
            j += 1
# Add remaining elements of arr1, if any
    while i < len(arr1):
        union_set.add(arr1[i])
        i += 1
# Add remaining elements of arr2, if any
    while j < len(arr2):
        union_set.add(arr2[j])
        j += 1

    return sorted(union_set)
arr1 = [1, 3, 4, 5, 6,7]
arr2 = [2, 3, 5, 6,8]
print(union_of_sorted_arrays(arr1, arr2))