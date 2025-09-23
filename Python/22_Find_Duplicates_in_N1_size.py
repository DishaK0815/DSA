class Solution:
    def Find_Duplicates_in_N_1_size_brute_force(self, nums):
        n = len(nums)
        duplicates = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and nums[i] not in duplicates:
                    duplicates.append(nums[i])
                    break 
        return duplicates
nums = [4,3,2,7,8,2,3,1]
print(Solution().Find_Duplicates_in_N_1_size_brute_force(nums))




class Solution2:
    def Find_Duplicates_in_N_1_size_optimal(self, nums):
        n = len(nums)
        duplicates = []
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicates.append(index + 1)
            else:
                nums[index] = -nums[index]
        return duplicates
    
nums = [4,3,2,7,8,2,3,1]
print(Solution2().Find_Duplicates_in_N_1_size_optimal(nums))




class Solution3:
    def Find_Duplicates_in_N_1_size_hashing(self, nums):
        n = len(nums)
        count = [0] * n
        duplicates = []
        for i in range(n):
            count[nums[i] - 1] += 1
            if count[nums[i] - 1] == 2:
                duplicates.append(nums[i])
        return duplicates
nums = [4,3,2,7,8,2,3,1]
print(Solution3().Find_Duplicates_in_N_1_size_hashing(nums))
