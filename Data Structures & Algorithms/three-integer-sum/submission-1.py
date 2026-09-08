class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0

        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                if total < 0:
                    l += 1
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            i += 1

        return res
            
            
