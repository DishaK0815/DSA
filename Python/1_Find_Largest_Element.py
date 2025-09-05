from functools import reduce

# Approach 1: Using built-in max() function
arr = [10, 4, 2, 99, 23, 56]
largest = max(arr)
print("Largest element (using max):", largest)
# time complexity: O(n)
# space complexity: O(1)



# Approach 2: Using a for loop
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("Largest element (using for loop):", largest)
# time complexity: O(n)
# space complexity: O(1)




# Approach 3: Using sort()
sorted_arr = sorted(arr)
largest = sorted_arr[-1]
print("Largest element (using sorted):", largest)
# time complexity: O(n log n)
# space complexity: O(n)




from typing import List
def sortArr(arr:list[int]) -> int:
    arr.sort()
    return arr[-1]
# time complexity: O(n log n)
# space complexity: O(1)



# Approach 4: Using reduce() from functools
largest = reduce(lambda a, b: a if a > b else b, arr)
print("Largest element (using reduce):", largest)
# time complexity: O(n)
# space complexity: O(1)




# Approach 5: Using recursion
def find_largest(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_largest(arr, n-1))
# time complexity: O(n)
# space complexity: O(n) due to recursion stack



arr = [10, 4, 2, 99, 23, 56]
largest = find_largest(arr, len(arr))
print("Largest element (using recursion):", largest)