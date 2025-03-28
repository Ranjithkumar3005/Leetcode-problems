class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            operations += 1

        # If target is smaller than startValue, just subtract the difference
        return operations + (startValue - target)
