class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = num
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if (mid * mid) > num:
                r = mid - 1
            elif (mid * mid) < num:
                l = mid + 1
            else:
                return True
        return False
