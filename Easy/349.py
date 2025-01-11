class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1 = {}
        h2 = {}
        for i in nums1:
            h1[i] = 1
        for j in nums2:
            h2[j] = 1
        d = []
        for i in h1:
            if i in h2:
                d.append(i)
        return d
