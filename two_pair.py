class Solution:
    def twoSum(self, nums, target):
        for j in range(len(nums)):
            copy = list(nums)
            copy.remove(nums[j])
            if (target - nums[j]) in copy:
                return j, nums.index(target - nums[j])




print(Solution().twoSum([1,2,2,3], 4))
