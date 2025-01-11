class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF  # 32 bit mask
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return (a & mask) if b > 0 else a
