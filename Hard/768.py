import collections
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if not stack or stack[-1] <= num:
                stack.append(num)
            else:
                element = stack[-1]
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(element)
        return len(stack)


class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr)):
            count[x] += 1
            if count[x] == 0:
                nonzero -= 1
            if count[x] == 1:
                nonzero += 1

            count[y] -= 1
            if count[y] == -1:
                nonzero += 1
            if count[y] == 0:
                nonzero -= 1

            if nonzero == 0:
                ans += 1

        return ans
