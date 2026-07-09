class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            value = target-nums[i]
            
            if value in index and index[value] != i:
                j = index[value]
                if i <= j:
                    return [i,j]
                else:
                    return [j,i]
            index[nums[i]] = i