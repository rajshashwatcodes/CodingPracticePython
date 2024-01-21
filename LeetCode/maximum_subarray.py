from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

sol = Solution()

nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Example 1 Output:", sol.maxSubArray(nums1))

nums2 = [1]
print("Example 2 Output:", sol.maxSubArray(nums2))

nums3 = [5, 4, -1, 7, 8]
print("Example 3 Output:", sol.maxSubArray(nums3))
