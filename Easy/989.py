class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        val = ""
        for i in num:
            val += str(i)
        tot = str(int(val) + k)
        arr = []
        for i in tot:
            arr.append(int(i))
        return arr
