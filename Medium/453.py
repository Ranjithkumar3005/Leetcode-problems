class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        sum = 0
        for i in range(1, len(nums)):
            sum += (nums[i - 1] - nums[i]) * i
        return sum


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        min_num = min(nums)
        for num in nums:
            moves += num - min_num

        return moves
