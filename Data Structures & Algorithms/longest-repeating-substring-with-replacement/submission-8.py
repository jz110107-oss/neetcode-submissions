class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        charcount = defaultdict(int)
        maxf = 0

        while r < len(s):
            charcount[s[r]] += 1
            maxf = max(maxf, charcount[s[r]])

            while r - l + 1 - maxf > k:
                charcount[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res


        