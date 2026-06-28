class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            key = "".join(sorted(x))
            if key in d:
                d[key].append(x)
            else:
                d[key] = [x]
        return list(d.values())

        # d = {}
        # for x in strs:
        #     d[x] = {}
        #     for y in x:
        #         if y in d[x]:
        #             d[x][y] += 1
        #         else:
        #             d[x][y] = 1
        # ans = []     
        # for x in d:
        #     i = None
        #     for y in ans:
        #         for z in y:
        #             if d[x].keys() == d[z].keys():
        #                 i = y
        #     if i is None:
        #         ans.append([x])
        #     else:
        #         i.append(x)
        # return ans