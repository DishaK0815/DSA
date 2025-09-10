# brute approach 
def find_missing_brute(arr,n):
    for num in range(1,n+1):
        if num not in arr:
            return num
        
arr = [1,2,3,5,6]
n = 6
print("Brute force:", find_missing_brute(arr,n))  # Output: 4

# better approach (using hashing / set)
def find_missing_better(arr,n):
    s =set(arr)
    for num in range(1, n+1):
        if num not in s:
            return num
arr = [1,2,3,5,6]
n = 6
print("Better (set):", find_missing_better(arr,n))  # Output: 4


# optimal approach (using sum formula)
def find_missing_optimal(arr,n):
    total = n * (n + 1) // 2
    return total - sum(arr)
arr = [1,2,3,5]
n = 5
print("Optimal (sum):", find_missing_optimal(arr,n))  # Output: 4