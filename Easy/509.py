class Solution:
    def fib(self, n: int) -> int:
        dum = [0, 1]
        val1 = 0
        val2 = 1
        for i in range(2, n + 1):
            tem = val2
            val2 = val1 + val2
            val1 = tem
            dum.append(val2)
        return dum[n]
