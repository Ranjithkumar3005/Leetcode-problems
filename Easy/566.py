class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        c1 = 0
        dum = []
        dum1 = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dum1.append(mat[i][j])
                c1 += 1
                if c1 == c:
                    dum.append(dum1)
                    dum1 = []
                    c1 = 0
        return dum
