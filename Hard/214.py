class Solution(object):
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        combined = s + "#" + rev_s

        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = compute_lps(combined)
        longest_palindromic_prefix_len = lps[-1]
        to_add = rev_s[: len(s) - longest_palindromic_prefix_len]
        return to_add + s
