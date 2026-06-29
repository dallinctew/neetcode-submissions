class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else: d[x] = 1
        print(d)
        l = []
        p = -1
        j = 0
        for i in range(k):
            for x in d:
                if d[x] >= j:
                    j = d[x]
                    p = x
                if list(d.keys())[-1] == x:
                    if p not in l:
                        l.append(p)
            d.pop(p, 0)
            j = 0
        return l