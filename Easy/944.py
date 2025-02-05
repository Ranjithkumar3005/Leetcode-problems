class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        dummy = []
        for i in range(0, len(strs[0])):
            for j in range(0, len(strs)):
                dummy.append(strs[j][i])
            if dummy != sorted(dummy):
                count += 1
            dummy = []
        return count
