class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        c = 0
        for i in s:
            if i == "(":
                st.append("(")
            else:
                if st:
                    st.pop()
                else:
                    c += 1
        if st:
            return c + len(st)
        return c
