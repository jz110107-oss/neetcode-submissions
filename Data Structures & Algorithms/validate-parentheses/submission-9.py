class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for char in s:
            if (char == "[" or char == "{" or char == "("):
                q.append(char)
            else:
                if len(q) == 0:
                    return False
                if not ((char ==  "}" and q[-1] == "{") or (char == "]" and q[-1] == "[") or (char == ")" and q[-1] == "(")):
                    return False
                else:
                    q.pop()
        return len(q) == 0

        