class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        answer = [float("inf")] * n

        # Left to right pass
        prev = float("-inf")
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = abs(i - prev)

        # Right to left pass
        prev = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))

        return answer
