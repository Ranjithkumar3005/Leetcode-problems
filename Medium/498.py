class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        h = {}
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if i + j not in h:
                    h[i + j] = []
                h[i + j].append(mat[i][j])
        ans = []
        for entry in h.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
