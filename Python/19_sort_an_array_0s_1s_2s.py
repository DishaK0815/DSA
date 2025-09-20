class Solution:
    def sort_an_array_0s_1s_2s_brute(self,nums):
        count0 = 0
        count1 = 0
        count2 = 0
        
        for i in nums:
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 += 1
            else:
                count2 += 1
        
        index = 0
        
        while count0 > 0:
            nums[index] = 0
            index += 1
            count0 -= 1
        
        while count1 > 0:
            nums[index] = 1
            index += 1
            count1 -= 1
        
        while count2 > 0:
            nums[index] = 2
            index += 1
            count2 -= 1
        
        return nums
nums = [2,0,2,1,1,0]
print(Solution().sort_an_array_0s_1s_2s_brute(nums))





class Solution:
    def sort_an_array_0s_1s_2s_optimal(self,nums):
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums
    
nums = [2,0,2,1,1,0]
print(Solution().sort_an_array_0s_1s_2s_optimal(nums))



class Solution:
    def sort_an_array_0s_1s_2s_better(self,nums):
        nums.sort()
        return nums
nums = [2,0,2,1,1,0]
print(Solution().sort_an_array_0s_1s_2s_better(nums))
