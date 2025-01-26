class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)[2:]
        for i in range(0, len(num) - 1):
            if num[i] == num[i + 1]:
                return False
        return True
