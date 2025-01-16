from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []  # No anagrams possible if `s` is shorter than `p`

        # Count the frequency of characters in `p`
        h1 = {}
        for char in p:
            h1[char] = h1.get(char, 0) + 1

        # Initialize frequency map for the first window in `s`
        h2 = {}
        for i in range(len(p)):
            h2[s[i]] = h2.get(s[i], 0) + 1

        # Store the starting indices of anagrams
        result = []
        if h1 == h2:
            result.append(0)

        # Slide the window over the rest of `s`
        for i in range(1, len(s) - len(p) + 1):
            # Remove the leftmost character of the previous window
            h2[s[i - 1]] -= 1
            if h2[s[i - 1]] == 0:
                del h2[s[i - 1]]

            # Add the rightmost character of the current window
            h2[s[i + len(p) - 1]] = h2.get(s[i + len(p) - 1], 0) + 1

            # Check if the current window is an anagram of `p`
            if h1 == h2:
                result.append(i)

        return result
