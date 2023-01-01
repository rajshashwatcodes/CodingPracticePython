class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f = {}
        for i in nums:
            if i in f:
                return True
            else:
                f[i] = 1
        return False
