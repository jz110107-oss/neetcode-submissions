class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlength = 1
        lookup = set(nums)
        start = []

        for n in nums:
            if n - 1 in lookup:
                continue
            else:
                start.append(n)
        
        for s in start:
            length = 1
            while s + 1 in lookup:
                length += 1
                s += 1
            maxlength = max(maxlength, length)
        return maxlength

        