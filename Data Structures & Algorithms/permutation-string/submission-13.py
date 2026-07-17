class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1list = [0] * 26
        s2list = [0] * 26

        for i in range(len(s1)):
            s1list[ord(s1[i]) - ord('a')] += 1
            s2list[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1list[i] == s2list[i]:
                matches += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')

            if s1list[index] == s2list[index]:
                matches -= 1
            s2list[index] += 1
            if s1list[index] == s2list[index]:
                matches += 1
            r += 1

            index = ord(s2[l]) - ord('a')
            if s1list[index] == s2list[index]:
                matches -= 1
            s2list[index] -= 1
            if s1list[index] == s2list[index]:
                matches += 1
            l += 1
        return matches == 26
      
            
            



        