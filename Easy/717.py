class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        # if len(bits)==1:
        #     return True

        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        if i != len(bits) - 1:
            return False
        return True
