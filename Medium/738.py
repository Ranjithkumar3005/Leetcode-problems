class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))  # Convert the number to a list of digits
        marker = len(digits)  # This will mark where to make changes

        # Traverse the digits from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                # If the current digit is smaller than the previous one
                digits[i - 1] = str(
                    int(digits[i - 1]) - 1
                )  # Decrease the previous digit
                marker = i  # Mark where the digits need to be turned to 9

        # Set all digits after the marker to 9
        for i in range(marker, len(digits)):
            digits[i] = "9"

        return int("".join(digits))  # Convert the list of digits back to an integer
