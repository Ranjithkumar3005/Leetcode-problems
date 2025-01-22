class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        prefix_sum = 0
        d = {0: 1}
        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in d:
                result = result + d[prefix_sum - k]
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1
        return result


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumdic = {}
        currsum = 0
        res = 0

        for num in nums:
            currsum += num
            if currsum not in sumdic:
                sumdic[currsum] = 1
            else:
                sumdic[currsum] += 1
            if currsum == k:
                res += 1
            if currsum - k in sumdic:
                res += sumdic[currsum - k]
                if k == 0:
                    res -= 1

        return res
