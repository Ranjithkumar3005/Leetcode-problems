class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert number to a list of digits
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find the first decreasing element from the end
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # If no such element is found, digits are in descending order
        if i == -1:
            return -1

        # Step 2: Find the smallest element larger than digits[i] to the right
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap the elements at i and j
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the digits to the right of i
        digits = digits[: i + 1] + digits[i + 1 :][::-1]

        # Convert back to integer
        result = int("".join(digits))

        # Step 5: Ensure it is within the 32-bit signed integer range
        return result if result <= (2**31 - 1) else -1
