class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                # Move both pointers if characters match
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                # If characters don't match, but current typed character is a repeat (long press)
                j += 1
            else:
                # If characters don't match and it's not a long press, return False
                return False

        # At the end, we should have checked all characters in `name`
        return i == len(name)
