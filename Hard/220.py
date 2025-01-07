from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        # SortedList to maintain the sliding window
        window = SortedList()

        for i in range(len(nums)):
            # Remove the element that is out of the window (indexDiff constraint)
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])

            # Use binary search to find the closest element in the current window
            pos = window.bisect_left(nums[i] - valueDiff)

            # Check if the current element is within the valueDiff range
            if pos < len(window) and abs(nums[i] - window[pos]) <= valueDiff:
                return True

            # Add the current number to the sliding window
            window.add(nums[i])

        return False
