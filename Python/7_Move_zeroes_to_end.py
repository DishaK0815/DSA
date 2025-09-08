# Brute force approach using extra space
def move_zero_brute(arr):
    result = [num for num in arr if num != 0]
    zeroes = [0]* (len(arr) - len(result))
    return result +zeroes
arr = [0,1,0,3,12]
print("Brute force:", move_zero_brute(arr))  # [1, 3, 12, 0, 0]


# Better approach using two pointers
def move_zero_better(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(j,n):
        arr[i] = 0
    return arr

arr = [0,1,0,3,12]
print("Better (two pointers):", move_zero_better(arr))  # [1, 3, 12, 0, 0]


# optimal approach 
def move_zero_optimal(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
arr = [0,1,0,3,12]
print("Optimal (in-place swap):", move_zero_optimal(arr))  # [1, 3, 12, 0, 0]
