class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        strs = ""
        h = {}
        for i in range(0, len(paragraph)):
            if paragraph[i] not in ["!", "?", "'", ";", "."]:
                if paragraph[i] == ",":
                    strs += " "
                else:
                    strs += paragraph[i].lower()
        dummy = strs.split(" ")
        for i in dummy:
            if i == "":
                dummy.remove("")
        for i in range(0, len(dummy)):
            if dummy[i] in banned:
                continue
            elif dummy[i] in h:
                h[dummy[i]] += 1
            else:
                h[dummy[i]] = 1
        for i in range(0, len(dummy)):
            if dummy[i] in h and h[dummy[i]] == max(h.values()):
                return dummy[i]
