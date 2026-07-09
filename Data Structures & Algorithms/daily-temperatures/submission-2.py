class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, i = stack.pop()
                ans[i] = index - i
            stack.append((temp, index))
        
        return ans
