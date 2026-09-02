class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_val = set()

        for num in nums:
            if num in seen_val:
                return True
            else:
                seen_val.add(num)
        
        return False
