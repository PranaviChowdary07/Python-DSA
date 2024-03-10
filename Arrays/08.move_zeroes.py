""" # Brute force
def move_zeroes(arr):
    i = 0
    while i < len(arr):
        if arr[i] ==0:
            arr.pop(i)
            arr.append(0)
        else:
            i+=1
arr = [0,3,0,5,0,7,9,0,0,8]
move_zeroes(arr)
print(arr)

#Another code:
def move_zeroes(arr):
    n = len(arr)
    for i in range(n):
        if arr[i]==0:
            j = j+1
            while j<n and arr[j]==0:
                j += 1
            if j<n :
                arr[i],arr[j] = arr[j], arr[i]
arr = [0,2,0,4,0,0,5,6,0,7]
move_zeroes(arr)
print(arr) """

# optimal solution:
def move_zeroes_toend(arr):
     i = 0
     for n in arr:
         if n != 0:
             arr[i] = n
             i +=1
     while i <len(arr):
         arr[i] = 0
         i +=1
arr = [0,4,5,0,0,3,1,0,0,6]
print("Original Array:",arr)
move_zeroes_toend(arr)
print(arr)
