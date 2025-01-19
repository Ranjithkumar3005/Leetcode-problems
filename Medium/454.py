class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        h = {}
        res = 0
        for i in nums1:
            for j in nums2:
                sum = i + j
                if sum not in h:
                    h[sum] = 1
                else:
                    h[sum] += 1

        for i in nums3:
            for j in nums4:
                s = i + j
                if -s in h:
                    res += h[-s]
        return res
