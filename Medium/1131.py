class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n = len(arr1)

        # Initialize variables for the four cases
        max1 = float("-inf")
        min1 = float("inf")
        max2 = float("-inf")
        min2 = float("inf")
        max3 = float("-inf")
        min3 = float("inf")
        max4 = float("-inf")
        min4 = float("inf")

        for i in range(n):
            val1 = arr1[i] + arr2[i] + i
            val2 = arr1[i] - arr2[i] + i
            val3 = -arr1[i] + arr2[i] + i
            val4 = -arr1[i] - arr2[i] + i

            max1 = max(max1, val1)
            min1 = min(min1, val1)
            max2 = max(max2, val2)
            min2 = min(min2, val2)
            max3 = max(max3, val3)
            min3 = min(min3, val3)
            max4 = max(max4, val4)
            min4 = min(min4, val4)

        # Compute the maximum value for each case
        result = max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)

        return result
