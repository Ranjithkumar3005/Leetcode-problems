class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        h = {}

        for i in words:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        sorted_words = sorted(h.keys(), key=lambda word: (-h[word], word))

        # Return the top k words
        return sorted_words[:k]
