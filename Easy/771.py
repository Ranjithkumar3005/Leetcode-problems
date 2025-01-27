class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total = 0
        for i in range(0, len(jewels)):
            total += stones.count(jewels[i])
        return total
