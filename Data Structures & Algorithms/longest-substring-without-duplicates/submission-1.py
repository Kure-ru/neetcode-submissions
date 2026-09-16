class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_map = {}
        l = 0
        max_l = 0

        for r in range(len(s)):
            if s[r] in s_map:
                l = max(s_map[s[r]] + 1, l)
            s_map[s[r]] = r
            max_l = max(max_l, r - l + 1)
        
        return max_l