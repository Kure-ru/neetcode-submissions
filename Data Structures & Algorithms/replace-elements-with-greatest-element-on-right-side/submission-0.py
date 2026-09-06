class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        res = [0] * l
        rightMax = -1

        for i in range(l - 1, -1, -1):
            res[i] = rightMax
            rightMax = max(arr[i], rightMax)
        
        return res