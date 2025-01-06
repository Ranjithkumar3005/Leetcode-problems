class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        result.append(str(integer_part))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        result.append(".")
        remainder_positions = {}
        while remainder != 0:
            if remainder in remainder_positions:
                start_index = remainder_positions[remainder]
                result.insert(start_index, "(")
                result.append(")")
                break
            remainder_positions[remainder] = len(result)
            remainder *= 10
            quotient = remainder // denominator
            result.append(str(quotient))
            remainder %= denominator

        return "".join(result)
