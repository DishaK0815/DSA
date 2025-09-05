# using temporary variable
def left_rotate_temp(arr):
    n= len(arr)
    temp =arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr
arr = [1,2,3,4,5]
print("left rotate temp:", left_rotate_temp(arr.copy()))


# using slicing
def left_rotate_slice(arr):
    return arr[1:] + arr[:1]
arr = [20,30,50,70,90]
print("left rotate slice:", left_rotate_slice(arr))




# using pop and append
def left_rotate_pop_append(arr):
    first = arr.pop(0)
    arr.append(first)
    return arr
arr1 = [100,200,300,400,500]
print("left rotate pop and append:", left_rotate_pop_append(arr1.copy()))
# time complexity: O(n)
# space complexity: O(1)



# if we want to rotate an array by k number
def rotate_by_k(arr2,k):
    n = len(arr2)
    k = k% n
    arr2[:] = arr2[-k:] + arr2[:-k] # right rotate
    # return arr2[k:] + arr2[:k] # left rotate
    return arr2

arr2 = [1,2,3,4,5,6,7]
k = 3
print("right rotate by k:", rotate_by_k(arr2,k))
# now changes taken place in arr2 as well

print("arr2 after right rotate by k:", arr2)

'''Example:
For arr2 = [1,2,3,4,5,6,7] and k = 3:

arr2[-3:] + arr2[:-3] → [5, 6, 7, 1, 2, 3, 4] (right rotate)
arr2[3:] + arr2[:3] → [4, 5, 6, 7, 1, 2, 3] (left rotate)


nums[-k:] gets the last k elements.
nums[:-k] gets all elements except the last k.
Concatenating them gives the rotated list.
nums[:] = ... assigns the new values to the original list, 
so the change is reflected outside the function.
'''
