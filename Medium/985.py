from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        sum1 = 0
        for i in nums:
            if i % 2 == 0:
                sum1 += i
        dum = []
        for i in queries:
            val = nums[i[1]]
            tot = val + i[0]
            nums[i[1]] = tot
            if val % 2 == 0:
                if tot % 2 == 0:
                    dum.append(sum1 - val + tot)
                    sum1 = sum1 - val + tot
                else:
                    dum.append(sum1 - val)
                    sum1 = sum1 - val
            else:
                if tot % 2 == 0:
                    dum.append(sum1 + tot)
                    sum1 += tot
                else:
                    dum.append(sum1)
        return dum
