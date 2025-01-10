class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max1 = 0
        word_sets = [set(word) for word in words]  # Create a list of sets for each word

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # Check if there is no common character using set intersection
                if not (word_sets[i] & word_sets[j]):
                    max1 = max(max1, len(words[i]) * len(words[j]))

        return max1
