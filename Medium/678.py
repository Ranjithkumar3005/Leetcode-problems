class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        for c in s:
            if c == "(" or c == "*":
                left += 1
            else:
                left -= 1
            if left < 0:
                return False

        right = 0
        for c in reversed(s):
            if c == ")" or c == "*":
                right += 1
            else:
                right -= 1
            if right < 0:
                return False

        return True
