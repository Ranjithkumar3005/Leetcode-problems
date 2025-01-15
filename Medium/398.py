class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.h = {}
        for i in range(0, len(nums)):
            if nums[i] in self.h:
                self.h[nums[i]].append(i)
            else:
                self.h[nums[i]] = [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        val = self.h[target][0]
        self.h[target].pop(0)
        self.h[target].append(val)
        return val


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
