class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        countT = Counter(t)
        countS = {}
        l = 0
        have, need = 0, len(countT)
        ans = (float("inf"), "")
        
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r], 0)
                if countS[s[r]] == countT[s[r]]:
                    have += 1
            while have == need:
                if r-l+1 < ans[0]:
                    ans = (r-l+1, s[l:r+1])

                if s[l] in countT:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1

               
        return ans[1]
            
