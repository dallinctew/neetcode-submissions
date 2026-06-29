class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else: d[x] = 1
        return sorted(d, key=lambda x: d[x], reverse=True)[:k]