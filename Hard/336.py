from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix != word and reversed_suffix in word_map:
                        result.append([word_map[reversed_suffix], i])

                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix != word and reversed_prefix in word_map:
                        result.append([i, word_map[reversed_prefix]])

        return result
