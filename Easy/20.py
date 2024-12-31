class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if not st:
                    return False
                if i == ")":
                    if st[-1] != "(":
                        return False
                if i == "}":
                    if st[-1] != "{":
                        return False
                if i == "]":
                    if st[-1] != "[":
                        return False
                st.pop()
        return not st
