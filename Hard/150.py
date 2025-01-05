from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                val2 = st.pop()
                val1 = st.pop()

                if i == "+":
                    st.append(val1 + val2)
                elif i == "-":
                    st.append(val1 - val2)
                elif i == "*":
                    st.append(val1 * val2)
                else:
                    st.append(int(val1 / val2))
            else:
                st.append(int(i))
        return st[0]
