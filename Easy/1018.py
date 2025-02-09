class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        s = ""
        dum = []
        for i in range(0, len(nums)):
            s += str(nums[i])
            val = int(s, 2)
            if val % 5 == 0:
                dum.append(True)
            else:
                dum.append(False)

        return dum
