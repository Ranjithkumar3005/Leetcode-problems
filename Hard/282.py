from typing import List


class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        res = []

        def dfs(i, path, cur_num, prevNum):
            if i == len(s):
                if cur_num == target:
                    res.append(path)
                return
            for j in range(i, len(s)):
                if j > i and s[i] == "0":
                    break
                num = int(s[i : j + 1])
                if i == 0:
                    dfs(j + 1, path + str(num), cur_num + num, num)
                else:
                    dfs(j + 1, path + "+" + str(num), cur_num + num, num)
                    dfs(j + 1, path + "-" + str(num), cur_num - num, -num)
                    dfs(
                        j + 1,
                        path + "*" + str(num),
                        cur_num - prevNum + prevNum * num,
                        prevNum * num,
                    )

        dfs(0, "", 0, 0)
        return res
