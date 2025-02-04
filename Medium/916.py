from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Create a max frequency map for words2
        h = {}
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                h[char] = max(h.get(char, 0), count)
        print(h)
        # Find all words in words1 that satisfy the frequency map
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= count for char, count in h.items()):
                result.append(word)

        return result
