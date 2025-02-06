class Solution(object):

    def maxTurbulenceSize(self, A):
        def cmp(x, y):
            return (x > y) - (x < y)

        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = cmp(A[i - 1], A[i])  # Gives -1,0,1
            if c == 0:
                anchor = i
            elif i == N - 1 or c * cmp(A[i], A[i + 1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
