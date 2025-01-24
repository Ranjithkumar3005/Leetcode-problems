class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        answer = []
        low, high = 1, n

        # Create the alternating pattern
        while low <= high:
            if k > 1:
                if k % 2 == 1:
                    answer.append(low)
                    low += 1
                else:
                    answer.append(high)
                    high -= 1
                k -= 1
            else:
                answer.append(low)
                low += 1

        return answer
