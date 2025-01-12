import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums1 = self.nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        self.nums1 = self.nums
        return self.nums1

    def shuffle(self):
        """
        :rtype: List[int]
        """
        self.nums1 = self.nums[:]
        for i in range(len(self.nums1) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums1[i], self.nums1[j] = self.nums1[j], self.nums1[i]
        return self.nums1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
