from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, arr):
            if index == len(num) and len(arr) >= 3:
                return arr

            current_num = 0
            for i in range(index, len(num)):
                if i > index and num[index] == "0":
                    break

                current_num = current_num * 10 + int(num[i])

                if current_num > 2**31 - 1:
                    break

                if len(arr) >= 2 and current_num > arr[-1] + arr[-2]:
                    break

                if len(arr) < 2 or current_num == arr[-1] + arr[-2]:
                    arr.append(current_num)
                    result = backtrack(i + 1, arr)
                    if result:
                        return result
                    arr.pop()

            return None

        result = backtrack(0, [])
        return result if result else []
