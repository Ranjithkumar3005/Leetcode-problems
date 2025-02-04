class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_left = nums[0]
        global_max = nums[0]
        partition_index = 0

        for i in range(1, len(nums)):
            if nums[i] < max_left:
                max_left = global_max
                partition_index = i
            else:
                global_max = max(global_max, nums[i])

        return partition_index + 1
