class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         res = max(res, min(heights[i], heights[j]) * (j - i))
        # return res

        i = 0
        j = len(heights) - 1

        while i < j:
            temp = min(heights[i], heights[j]) * (j - i)
            res = max(res, temp)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
        return res