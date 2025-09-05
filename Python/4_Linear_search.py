def Linear_search(arr, target,n):
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

arr = [12,345,86,95,96,3]
target = 345
n = len(arr)
print("Target at location : ", Linear_search(arr,target,n))

# time complexity: O(n)
# space complexity: O(1)