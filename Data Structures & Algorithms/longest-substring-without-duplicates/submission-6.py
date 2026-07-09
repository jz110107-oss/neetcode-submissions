class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        count = 0
        unique = set()

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            count = max(count, r - l + 1)
        return count

