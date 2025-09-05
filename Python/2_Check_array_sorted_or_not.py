from itertools import pairwise

# Method 1: Using a simple loop
def is_sorted_loop(arr):
    for i in range(len(arr) -1):
        if arr[i] > arr[i+1]:
            return False
    return True
# time complexity: O(n)
# space complexity : O(1)


    


# Method 2: Using all() with generator expression

def is_sorted_all(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
#time complexity : O(n)
# space complexity : O(1)


def is_sorted_all(arr):
    return all(arr[i] <= arr[i+1] for i in range(len[arr]))



# Method 3: Comparing with sorted version

def is_sorted_sorted(arr):
    return arr == sorted(arr)
# time complexity : O(n log n)
# space complexity : O(n)




# Method 4: Using itertools.pairwise (Python 3.10+)

def is_sorted_pairwise(arr):
    return all(x <= y for x, y in pairwise(arr))
# time complexity : O(n)
# space complexity : O(1)


# Example usage
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 2, 1]

    print(is_sorted_loop(arr1))      # True
    print(is_sorted_all(arr2))       # False
    print(is_sorted_sorted(arr1))    # True
    print(is_sorted_pairwise(arr2))  # False