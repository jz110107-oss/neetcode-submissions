class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "/"
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        countstring = ""
        count = 0
        while i < len(s):
            if s[i] != "/":
                countstring += s[i]
                i += 1
            else:
                count = int(countstring)
                countstring = ""
                decoded.append(s[i+1:i+1+count])
                i += 1 + count
        return decoded



            



