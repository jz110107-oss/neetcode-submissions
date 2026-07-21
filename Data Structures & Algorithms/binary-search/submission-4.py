class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l <= r:
            middle = (l + r)//2

            if not (middle < len(nums) and middle >= 0):
                return -1

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return -1
        