class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}
        for i in range(len(nums)):
            corresponding = target - nums[i]
            if corresponding in match and match[corresponding] != i:
                return [match[corresponding], i]
            else:
                match[nums[i]] = i
        