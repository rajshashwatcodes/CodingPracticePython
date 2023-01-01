class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        for i in range(0,len(nums)):
            cur_sum = 0
            for j in range(i,len(nums)):
                cur_sum += nums[j] 
                ans = max(ans,cur_sum)
        return ans
