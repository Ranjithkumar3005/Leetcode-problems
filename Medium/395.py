class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # If the length of the string is less than k, return 0
        if len(s) < k:
            return 0

        # Count the frequency of each character in the string
        char_freq = {}
        for char in s:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1

        # Find the index of the first character with a frequency less than k
        for i, char in enumerate(s):
            if char_freq[char] < k:
                # Split the string into two parts and recursively find the longest substring in each part
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1 :], k)
                # Return the maximum length of the two substrings
                return max(left, right)

        # If all characters have a frequency greater than or equal to k, return the length of the string
        return len(s)
