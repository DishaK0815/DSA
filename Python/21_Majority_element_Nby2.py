class Solution:
    def MajorityElement_occurs_more_than_Nby2(self,nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
nums = [3,2,3]
print(Solution().MajorityElement_occurs_more_than_Nby2(nums))


class Solution2:
    def MajorityElement_occurs_more_than_Nby2(self,nums):
        nums.sort()
        return nums[len(nums)//2]
nums = [2,2,1,1,1,2,2]
print(Solution2().MajorityElement_occurs_more_than_Nby2(nums))



class Solution3:
    def MajorityElement_occurs_more_than_Nby2(self,nums):
        from collections import Counter
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
nums = [2,2,1,1,1,2,2]
print(Solution3().MajorityElement_occurs_more_than_Nby2(nums))
