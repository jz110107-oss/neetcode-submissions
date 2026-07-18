class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []

        for token in tokens:
            if token == "+":
                second = ops.pop()
                first = ops.pop()
                ops.append(first + second)
            elif token == "-":
                second = ops.pop()
                first = ops.pop()
                ops.append(first - second)
            elif token == "*":
                second = ops.pop()
                first = ops.pop()
                ops.append(first * second)
            elif token == "/":
                second = ops.pop()
                first = ops.pop()
                ops.append(int(first / second))
            else:
                ops.append(int(token))
        return ops[-1]

        