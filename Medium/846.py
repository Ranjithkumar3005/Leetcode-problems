import collections


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        sorted_num = sorted(count.keys())

        for num in sorted_num:
            if count[num] > 0:
                for j in range(1, groupSize):
                    if (num + j not in count) or (count[num + j] < count[num]):
                        return False
                    else:
                        count[num + j] = count[num + j] - count[num]

                count[num] = 0

        for c in count.values():
            if c > 0:
                return False

        return True
