from cmath import sqrt


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        ps = [(i + 1) * (i + 1) for i in range(int(sqrt(n)))]
        q = set([n])
        level = 0
        while q:
            level += 1
            next_q = set()
            breadth = len(q)
            for i in range(breadth):
                cur = q.pop()
                for num in ps:
                    if num == cur:
                        return level
                    elif num > cur:
                        break
                    else:
                        next_q.add(cur - num)
            q = next_q
        return level
