class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        h = {}
        for char in t:
            h[char] = h.get(char, 0) + 1

        left = 0
        right = 0
        formed = 0
        required = len(h)
        h1 = {}
        min_len = float("inf")
        min_window = ""

        while right < len(s):
            char = s[right]
            if char in h:
                h1[char] = h1.get(char, 0) + 1
                if h1[char] == h[char]:
                    formed += 1

            while left <= right and formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left : right + 1]

                char = s[left]
                if char in h1:
                    h1[char] -= 1
                    if h1[char] < h[char]:
                        formed -= 1
                left += 1

            right += 1

        return min_window
