class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        spli = path.split("/")

        for i in range(0, len(spli)):
            if spli[i] == "" or spli[i] == ".":
                continue
            elif spli[i] == "..":
                if st:
                    st.pop()
            else:
                st.append(spli[i])

        return "/" + "/".join(st)
