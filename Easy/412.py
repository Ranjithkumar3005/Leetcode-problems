class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dummy = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                dummy.append("FizzBuzz")
            elif i % 3 == 0:
                dummy.append("Fizz")
            elif i % 5 == 0:
                dummy.append("Buzz")
            else:
                dummy.append(str(i))
        return dummy
