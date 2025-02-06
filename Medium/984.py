class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        while a > 0 or b > 0:
            if a > b:
                if a > 1:
                    result.append("aa")
                    a -= 2
                else:
                    result.append("a")
                    a -= 1
                if b > 0:
                    result.append("b")
                    b -= 1
            elif b > a:
                if b > 1:
                    result.append("bb")
                    b -= 2
                else:
                    result.append("b")
                    b -= 1
                if a > 0:
                    result.append("a")
                    a -= 1
            else:
                if a > 0:
                    result.append("a")
                    a -= 1
                if b > 0:
                    result.append("b")
                    b -= 1

        return "".join(result)


# Example usage:
# sol = Solution()
# print(sol.strWithout3a3b(5, 3))  # Output: "aabaab" or another valid variation
