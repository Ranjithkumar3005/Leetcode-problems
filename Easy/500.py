class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = "qwertyuiop"
        line2 = "asdfghjkl"
        line3 = "zxcvbnm"
        store = []

        for k in words:

            if len(set(line1 + k.lower())) == len(line1):
                store.append(k)
            if len(set(line2 + k.lower())) == len(line2):
                store.append(k)
            if len(set(line3 + k.lower())) == len(line3):
                store.append(k)
        return store
