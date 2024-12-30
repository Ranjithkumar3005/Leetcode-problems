class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        length = len(arr)
        if length % 2 == 1:
            return arr[length // 2]
        else:
            return (arr[length // 2 - 1] + arr[length // 2]) / 2.0
