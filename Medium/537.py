class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = map(int, num1[:-1].split("+"))
        real2, imaginary2 = map(int, num2[:-1].split("+"))

        real_result = real1 * real2 - imaginary1 * imaginary2
        imaginary_result = real1 * imaginary2 + imaginary1 * real2

        return f"{real_result}+{imaginary_result}i"
