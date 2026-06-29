class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for x in d:
            buckets[d[x]].append(x)
        
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for x in buckets[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans