def array_rotated_and_sorted_brute(arr):
    n = len(arr)
    for i in range(n):
        rotated = arr[i:] + arr[:i]
        if rotated == sorted(arr):
            return True
    return False
arr = [3, 4, 5, 1, 2]
print("Brute force:", array_rotated_and_sorted_brute(arr))  # Output: True

# optimal approach
def array_rotated_and_sorted_optimal(arr):
    n = len(arr)
    count = 0 
    for i in range(n):
        if arr[i] > arr[(i+1)% n]:
            count += 1
        return count > 1
arr = [3,4,5,1,2]
print("optimal : ", array_rotated_and_sorted_optimal(arr))