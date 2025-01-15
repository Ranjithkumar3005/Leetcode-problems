class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # If num is negative, convert to positive by adding 2^32
        if num < 0:
            num += 2**32

        return hex(num)[2:]  # Remove '0x' prefix
