from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ops = operations
        for i in range(0, len(ops)):
            if ops[i].lstrip("-").isdigit():
                st.append(int(ops[i]))
            elif ops[i] == "C":
                st.pop()
            elif ops[i] == "D":
                val = st[-1] * 2
                st.append(val)
            else:
                val1 = st[-1] + st[len(st) - 2]
                st.append(val1)
            print(st)
        return sum(st)
