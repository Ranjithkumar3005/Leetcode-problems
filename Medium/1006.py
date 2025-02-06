class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        operation = 0  # 0: *, 1: /, 2: +, 3: -

        while n > 0:
            if operation == 0:
                stack[-1] *= n
            elif operation == 1:
                stack[-1] = int(stack[-1] / n)  # Floor division
            elif operation == 2:
                stack.append(n)
            else:  # operation == 3
                stack.append(-n)
            n -= 1
            operation = (operation + 1) % 4

        return sum(stack)
