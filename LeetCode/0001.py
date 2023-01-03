class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            nums[i] = None
            if remaining in nums:
                return [i, nums.index(remaining)]
