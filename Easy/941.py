class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)

        if n < 3:
            return False

        i = 0

        # Ascend to the peak
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # If there's no ascent or we're at the first or last element
        if i == 0 or i == n - 1:
            return False

        # Descend from the peak
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        # Check if we reached the end of the array
        return i == n - 1
