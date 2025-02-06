from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        val = arr[:]
        dum = sorted(arr)
        arr = []
        while val != []:
            max1 = max(val)
            idx = dum.index(max1)
            idx1 = val.index(max1)
            if idx != idx1:
                if idx1 != 0:
                    val = val[: idx1 + 1][::-1] + val[idx1:]
                    arr.append(idx1 + 1)
                val = val[::-1]
                arr.append(idx + 1)
            val.remove(max1)
        return arr
