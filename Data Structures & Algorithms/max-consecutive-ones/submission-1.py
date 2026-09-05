class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = c = 0
        for num in nums:
            c = c + 1 if num else 0
            res = max(res, c)
        return res