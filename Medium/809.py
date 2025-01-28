from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # Helper function to compress the string and return its groups and their counts
        def compress(word):
            groups, counts = [], []
            count = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    count += 1
                else:
                    groups.append(word[i - 1])
                    counts.append(count)
                    count = 1
            groups.append(word[-1])
            counts.append(count)
            return groups, counts

        # Compress the target string `s`
        s_groups, s_counts = compress(s)
        result = 0

        # Check each word in words
        for word in words:
            word_groups, word_counts = compress(word)

            # Check if the word has the same groups as `s`
            if word_groups != s_groups:
                continue

            # Validate each group count
            stretchy = True
            for i in range(len(word_counts)):
                if s_counts[i] < 3 and s_counts[i] != word_counts[i]:
                    stretchy = False
                    break
                if s_counts[i] >= 3 and s_counts[i] < word_counts[i]:
                    stretchy = False
                    break

            if stretchy:
                result += 1

        return result
