# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        i = 1
        j = n
        while i < j:
            pivot = (i + j) // 2
            if isBadVersion(pivot):
                j = pivot  # keep track of the leftmost bad version
            else:
                i = pivot + 1  # the one after the rightmost good version
        return i
