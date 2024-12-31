class Solution:
    def countAndSay(self, n: int) -> str:
        def loop(s):
            result = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(s[i - 1])
                    count = 1

            result.append(str(count))
            result.append(s[-1])
            return "".join(result)

        current = "1"
        for _ in range(1, n):
            current = loop(current)

        return current
