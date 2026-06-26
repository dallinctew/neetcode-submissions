class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if target/2 in d and d.get(x) != i and x == target/2:
                print("special")
                return[d.get(target/2),i]
            d.update({x: i})
        for x in d:
            if target -x in d and d.get(x) != d.get(target-x):
                i = d.get(x)
                j = d.get(target - x)
                return [int(i), int(j)]
        return []

        # i = j = None
        # for x in nums:
        #     y = target - x
        #     if y in nums[nums.index(x)+1:]:
        #         i = nums.index(x)
        #         nums.pop(i)
        #         return [i, nums.index(y)+1]
        # return []