class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones)
        while len(stones) > 1:
            val1 = stones.pop()
            val2 = stones.pop()
            if val1 != val2:
                stones.append(val1 - val2)
                stones = sorted(stones)
        if stones == []:
            return 0
        return stones[0]
