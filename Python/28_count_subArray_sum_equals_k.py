class Solution:
    def Count_subArray_sum_equals_k(self,nums,k):
        n = len(nums)
        cnt = 0  

        for i in range(n):  
            for j in range(i, n): 
                subarray_sum = sum(nums[i:j+1])
                if subarray_sum == k:
                    cnt += 1
        return cnt
    
nums = [1,3,5,2,6,7]
k = 8
sol = Solution()
print(sol.Count_subArray_sum_equals_k(nums,k))


# better approach
class Solution:
    def count_SubArray_sum_equals_k(self,nums,k):
        n = len(nums)
        cnt = 0

        for i in range(n):
            sub_array = 0
            for j in range(i,n):
                print(nums[j])
                sub_array += nums[j]

                if sub_array == k:
                    cnt += 1
        return cnt

nums = [1,3,5,2,6]
k = 8
sol = Solution()
print(sol.count_SubArray_sum_equals_k(nums,k))



# optimal approach
from collections import defaultdict
class Solution:
    def count_subarray_sum_equals_k(self,nums,k):
        n = len(nums)
        mpp = defaultdict(int)
        cnt = 0
        presum = 0
        mpp[0] = 1
        for i in range(n):
            presum += nums[i]
            remove = presum - k
            cnt += mpp[remove]
            mpp[presum] += 1
        return cnt
    
nums = [1,3,5,6,2,8]
k = 8
sol = Solution()
print(sol.count_subarray_sum_equals_k(nums,k))
