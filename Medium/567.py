class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, return False
        if len(s1) > len(s2):
            return False

        # Frequency map of characters in s1
        h1 = {}
        for char in s1:
            h1[char] = h1.get(char, 0) + 1

        # Initialize frequency map for the first window in s2
        n = len(s1)
        h2 = {}
        for i in range(n):
            h2[s2[i]] = h2.get(s2[i], 0) + 1

        # Check if the first window is a permutation
        if h1 == h2:
            return True

        # Slide the window across s2
        for i in range(n, len(s2)):
            # Remove the leftmost character of the previous window
            left_char = s2[i - n]
            h2[left_char] -= 1
            if h2[left_char] == 0:
                del h2[left_char]

            # Add the new character to the current window
            h2[s2[i]] = h2.get(s2[i], 0) + 1

            # Check if the current window is a permutation
            if h1 == h2:
                return True

        return False
