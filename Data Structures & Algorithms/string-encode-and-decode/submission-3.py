class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "#" + strs[i]
        return string
    
    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:(j+1+length)])
            i = j + 1 + length
        return strs
            

