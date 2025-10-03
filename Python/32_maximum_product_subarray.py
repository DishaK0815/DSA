

def maxProductSubArray(nums):
    result = float('-inf')
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            result = max(result, prod)
    return result

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))




def maxProductSubArray(nums):
    result = nums[0]
    for i in range(len(nums) - 1):
        p = nums[i]
        for j in range(i + 1, len(nums)):
            result = max(result, p)
            p *= nums[j]
        result = max(result, p)  # manages (n-1)th term
    return result

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))




def maxProductSubArray(arr):
    n = len(arr) # size of array.

    pre, suff = 1, 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, max(pre, suff))
    return ans

arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", maxProductSubArray(arr))


def maxProductSubArray(nums):
    prod1 = nums[0]
    prod2 = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod1 = temp

        result = max(result, prod1)

    return result

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))
