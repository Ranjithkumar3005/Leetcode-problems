class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {5: 0, 10: 0, 20: 0}
        for b in bills:
            d[b] += 1
            if b == 10:
                if d[5] > 0:
                    d[5] -= 1
                else:
                    return False
            elif b == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] > 2:
                    d[5] -= 3
                else:
                    return False
        return True
