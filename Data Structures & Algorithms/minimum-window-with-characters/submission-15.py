class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = Counter(t)
        matches = 0
        minlen = [float("inf"), 0, 0]
        l, r = 0, 0

        while r < len(s):
            if s[r] in tcount:
                if tcount[s[r]] > 0:
                    matches += 1
                tcount[s[r]] -= 1
            while matches == len(t):
                if minlen[0] > r - l + 1:
                    minlen[0] = r - l + 1
                    minlen[1] = l
                    minlen[2] = r
                if s[l] in tcount:
                    tcount[s[l]] += 1
                    if tcount[s[l]] > 0:
                        matches -= 1
                l += 1
            r += 1

        if minlen[0] == float("inf"):
            return ""
        return s[minlen[1]:minlen[2]+1]
            
                    
        