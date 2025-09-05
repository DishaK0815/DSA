# find the second largest and second smallest element in an array
def second_largest(arr,n):
    first = second = float('-inf')

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    if second == float('-inf'):
        return -1
    else:
        return second
    
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print("second Largest element is :" , second_largest(arr, n))
# time complexity: O(n)
# space complexity: O(1)




def second_smallest(arr,n):
    first = second = float('inf')
    for i in range(n):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i]!= first:
            second = arr[i]
    if second == float('inf'):
        return -1
    else:
        return second
arr = [12, 35, 1, 10, 34, 1]
n=len(arr)
print("second smallest element is :" , second_smallest(arr,n))
# time complexity : O(n)
# space complexity : O(1)