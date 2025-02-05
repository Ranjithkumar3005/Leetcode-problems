class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        st = []

        c = 0
        for i in range(0, len(pushed)):
            st.append(pushed[i])
            while True:
                if st == []:
                    break
                if st != [] and st[-1] == popped[c]:
                    st.pop()
                    c += 1
                else:
                    break
        if st == []:
            return True
        return False
