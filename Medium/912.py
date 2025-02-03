class Solution:
    def sortArray(self, nums):
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) > 1:

            mid = len(nums) // 2

            left_half = nums[:mid]
            right_half = nums[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1
        return nums


nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]

solution = Solution()
print(solution.sortArray(nums1))  # Output: [1, 2, 3, 5]
print(solution.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]
