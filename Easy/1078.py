class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        thirds = []
        words = text.split()
        for index, word in enumerate(words):
            print(index, " ", word)
            if index < len(words) - 2:
                if word == first and words[index + 1] == second:
                    thirds.append(words[index + 2])
        return thirds
