class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        max_len = 0
        for i in range(0, len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_len = max(max_len, i - st[-1])
        return max_len
