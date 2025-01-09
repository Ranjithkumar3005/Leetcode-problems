class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        h1 = {}  # Map from pattern to words
        h2 = {}  # Map from words to pattern

        for i in range(len(pattern)):
            if pattern[i] in h1:
                if h1[pattern[i]] != words[i]:
                    return False
            else:
                h1[pattern[i]] = words[i]

            if words[i] in h2:
                if h2[words[i]] != pattern[i]:
                    return False
            else:
                h2[words[i]] = pattern[i]

        return True
