class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                index = stack.pop()[1]
                res[index] = i - index
            if not stack or stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i], i))
            
        return res
                