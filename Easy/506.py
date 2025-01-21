class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(score, reverse=True)
        place = {}
        out = []

        for i in range(len(score)):
            if i == 0:
                place[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                place[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                place[sorted_score[i]] = "Bronze Medal"
            else:
                place[sorted_score[i]] = str(i + 1)

        for i in score:
            out.append(place[i])
        return out
