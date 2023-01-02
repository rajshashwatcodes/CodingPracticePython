class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lis = []
        sum = 0
        for i in nums:
            sum+=i
            lis.append(sum)
        return lis
