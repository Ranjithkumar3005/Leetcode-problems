class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        maximize profit
        """
        total = 0
        hm = {}
        for i in range(len(profit)):
            if profit[i] in hm:
                hm[profit[i]] = min(hm[profit[i]], difficulty[i])
            else:
                hm[profit[i]] = difficulty[i]

        profit.sort()
        worker.sort()

        profit_ind = len(profit) - 1
        # traverse from the back of both
        for i in range(len(worker) - 1, -1, -1):
            while profit_ind > -1:
                if worker[i] >= hm[profit[profit_ind]]:
                    total += profit[profit_ind]
                    break
                profit_ind -= 1

        return total
