class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = None
        for x in nums:
            y = target - x
            if y in nums[nums.index(x)+1:]:
                i = nums.index(x)
                nums.pop(i)
                return [i, nums.index(y)+1]
        return []


        