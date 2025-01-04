class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        prev_num = None
        nums = list(set(nums))
        nums.sort()
        # print(nums)
        for num in nums:
            if prev_num is not None:
                if num == prev_num + 1:
                    count = count + 1
                else:
                    if count > max_count:
                        max_count = count
                    count = 1
            else:
                count = 1
            prev_num = num
            # print(num, count)
        return max(count, max_count)


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        c = 1
        max = 1
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        for i in nums:
            if i in h:
                continue
            if i - 1 in h:
                c += 1
                h[i] = 1
            else:
                if max < c:
                    max = c
                h = {}
                c = 1
                h[i] = 1
        if max < c:
            max = c

        return max
