class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxCount = 0
        count = 0

        for number in numbers:
            if number - 1 not in numbers:
                temp = number
                while temp in numbers:
                    count += 1
                    temp += 1
                maxCount = max(maxCount, count)
                count = 0
        return maxCount


                