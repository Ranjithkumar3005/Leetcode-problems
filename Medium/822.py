class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        bad_numbers = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}

        result = float("inf")

        for i in range(len(fronts)):
            if fronts[i] not in bad_numbers:
                result = min(result, fronts[i])
            if backs[i] not in bad_numbers:
                result = min(result, backs[i])

        return result if result != float("inf") else 0
