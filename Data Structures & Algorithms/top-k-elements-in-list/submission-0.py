class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       bucket = [[] for _ in range(len(nums) + 1)]

       for value, n in count.items():
            bucket[n].append(value)

       high_freq = reversed(bucket)

       res = []
       for item in high_freq:
            if len(res) >= k:
                return res
            if item:
                res.extend(item)

       return res