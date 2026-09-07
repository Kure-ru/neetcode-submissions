class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        streak = 0

        for num in numSet:
            if num - 1 not in numSet:
                seq = 1
                while (num + seq) in numSet:
                    seq += 1
                streak = max(streak, seq)
        
        return streak