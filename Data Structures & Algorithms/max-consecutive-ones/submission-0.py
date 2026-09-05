class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max = 0 

        for num in nums:
            if num == 1:
                c += 1
            else:
                if c > max:
                    max = c
                c = 0
        
        if c > max:
            max = c
            
        return max