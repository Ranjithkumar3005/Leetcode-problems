class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        S = s.replace("-", "")

        head = len(S) % k

        grouping = []

        if head:
            grouping.append(S[:head])

        for index in range(head, len(S), k):
            grouping.append(S[index : index + k])

        return "-".join(grouping).upper()
