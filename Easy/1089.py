class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr1 = arr[:]
        i = 0
        j = 0
        while j < len(arr):
            arr[j] = arr1[i]
            if arr1[i] == 0 and j + 1 < len(arr):
                j += 1
                arr[j] = 0
            i += 1
            j += 1
