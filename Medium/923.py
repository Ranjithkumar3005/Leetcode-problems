class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        count = 0
        MOD = 10**9 + 7

        for i in range(len(arr)):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                total = arr[i] + arr[j] + arr[k]
                if total == target:
                    # Count duplicates for j and k
                    if arr[j] == arr[k]:
                        count += (k - j + 1) * (k - j) // 2
                        break
                    else:
                        left_count = 1
                        right_count = 1
                        while j + 1 < k and arr[j] == arr[j + 1]:
                            left_count += 1
                            j += 1
                        while k - 1 > j and arr[k] == arr[k - 1]:
                            right_count += 1
                            k -= 1
                        count += left_count * right_count
                        j += 1
                        k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1

        return count % MOD
