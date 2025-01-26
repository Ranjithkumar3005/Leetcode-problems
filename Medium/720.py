from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Create a set for efficient prefix lookup
        word_set = set(words)
        longest_word = ""

        # Sort words lexicographically
        words.sort()

        for word in words:
            # Check if all prefixes of the word exist
            is_valid = True
            for k in range(1, len(word)):  # Check all prefixes
                if word[:k] not in word_set:
                    is_valid = False
                    break

            # If the word is valid and longer than the current longest word
            if is_valid:
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word
