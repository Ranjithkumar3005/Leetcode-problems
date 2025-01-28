class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(set(words), key=len, reverse=True)
        encoding_set = set()
        total_length = 0

        for word in words:
            if word not in encoding_set:
                total_length += len(word) + 1
                for i in range(len(word)):
                    encoding_set.add(word[i:])

        return total_length
