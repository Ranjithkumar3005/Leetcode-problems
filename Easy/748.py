class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        chars = {}
        for char in licensePlate:
            if char.isalpha():
                chars[char.lower()] = chars.get(char.lower(), 0) + 1

        words.sort(key=len)

        for word in words:
            allCharsInWord = True

            for char in chars:
                if (char not in word) or (word.count(char) < chars[char]):
                    allCharsInWord = False
                    break

            if allCharsInWord == True:
                return word
