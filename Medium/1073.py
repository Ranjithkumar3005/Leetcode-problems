class Solution(object):
    def addNegabinary(self, arr1, arr2):
        result = []
        carry = 0
        i = len(arr1) - 1
        j = len(arr2) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                bit1 = arr1[i]
            else:
                bit1 = 0
            if j >= 0:
                bit2 = arr2[j]
            else:
                bit2 = 0

            total = bit1 + bit2 + carry

            result.append(total % 2)

            carry = -(total // 2)

            i -= 1
            j -= 1

        # Remove the leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]
