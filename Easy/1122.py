class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        h = {}
        for i in arr1:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        dum = []
        for i in arr2:
            for j in range(0, h[i]):
                dum.append(i)
            h[i] = 0
        dum1 = []
        for i in h:
            if h[i] != 0:
                for j in range(0, h[i]):
                    dum1.append(i)
        dum1 = sorted(dum1)
        return dum + dum1
