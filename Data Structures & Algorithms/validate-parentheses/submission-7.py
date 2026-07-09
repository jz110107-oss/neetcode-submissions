class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for string in s:
            if string == "(" or string == "{" or string == "[":
                stack.append(string)
            else:
                if not stack:
                    return False
                openstring = stack.pop()
                if openstring == "(" and string != ")" or openstring == "{" and string != "}" or openstring == "[" and string != "]":
                    return False
        if stack:
            return False
        return True
        