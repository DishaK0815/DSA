# brute force approach 
def max_consecutive_ones_brute(arr):
    max_count = 0
    n = len(arr)
    for i in range(n):
        count = 0
        for  j in range(i,n):
            if arr[j] == 1:
                count += 1
                max_count = max(max_count , count)
            else:
                break
    return max_count
arr = [1,1,0,1,1,1]
print("Brute force:", max_consecutive_ones_brute(arr))  # Output: 3


# better approach ( using single loop)
def max_consecutive_ones_better(arr):
    max_count = 0
    count = 0
    for i in arr:
        if  i == 1:
            count += 1
            max_count = max(max_count , count)
        else:
            count = 0
    return max_count
arr = [1,1,0,1,1,1]
print("Better:", max_consecutive_ones_better(arr))  # Output: 3






