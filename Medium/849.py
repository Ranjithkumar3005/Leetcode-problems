class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dis = -1
        num_seats = len(seats)
        prev = -1
        for i in range(0, num_seats):
            if seats[i] == 1:
                if prev == -1 and seats[0] == 0:
                    cur_dis = i - prev - 1
                    max_dis = max(max_dis, cur_dis * 2 + 1)
                else:
                    max_dis = max(max_dis, i - prev)
                prev = i
            elif i == num_seats - 1:
                cur_dis = i - prev
                max_dis = max(max_dis, cur_dis * 2 + 1)
        return max_dis / 2
