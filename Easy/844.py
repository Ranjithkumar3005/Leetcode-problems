class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st1 = []
        st2 = []
        for i in s:
            if i == "#" and st1 != []:
                st1.pop()
            elif i == "#":
                continue
            else:
                st1.append(i)
        for i in t:
            if i == "#" and st2 != []:
                st2.pop()
            elif i == "#":
                continue
            else:
                st2.append(i)
        print(st1, " ", st2)
        if st1 == st2:
            return True
        return False
