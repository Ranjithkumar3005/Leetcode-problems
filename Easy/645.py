class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [True for _ in range(len(nums) + 1)]
        for i in nums:
            a[i] = False
        print(a)
        s_ = list(set(nums))

        def freq(nums):
            freq = {}
            for item in nums:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1
                if freq[item] == 2:
                    return item

        # print(freq(nums))
        for i in range(0, len(a)):
            if a[i] == True and i != 0:
                print(i)
                return [freq(nums), i]
