class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        seen = [False] * n
        ans = 0

        for num in range(2, n):
            if seen[num]:
                continue
            ans += 1
            for mult in range(num * num, n, num):
                seen[mult] = True

        return ans
