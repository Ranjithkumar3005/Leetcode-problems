class Solution(object):
    def commonChars(self, words):
        result = []
        if len(words) < 2:
            words = "".join(i for i in words)
            for i in words:
                result.append(i)

            return result

        res = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res
