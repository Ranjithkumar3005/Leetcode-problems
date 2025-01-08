class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        c = 0
        for i in range(0, len(citations)):
            if citations[i] >= i + 1:
                c += 1
            else:
                break
        return c
