# kadane's algorithm
class solution:
    def max_subarray_sum(self,arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(solution().max_subarray_sum(arr))


class Solution:
    def max_subarray_sum_optimized(self, arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum =  max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().max_subarray_sum_optimized(arr))


class Solution:
    def max_subarray_sum_divide_and_conquer(self,arr):
        def helper(left, right):
            if left == right:
                return arr[left]
            mid = (left + right) // 2
            left_max = helper(left,mid)
            right_max = helper(mid+1, right)
            cross_max = cross_sum(left, mid, right)
            return max(left_max, right_max, cross_max)
        
        def cross_sum(left, mid, right):
            if left == right:
                return arr[left]
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left-1, -1):
                current_sum += arr[i]
                left_sum = max(left_sum, current_sum)
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid+1, right+1):
                current_sum += arr[i]
                right_sum = max(right_sum, current_sum)
            return left_sum + right_sum
        return helper(0, len(arr)-1)
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().max_subarray_sum_divide_and_conquer(arr))


