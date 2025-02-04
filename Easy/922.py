class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        even_index = 0  # Pointer for even indices
        odd_index = 1  # Pointer for odd indices

        while even_index < n and odd_index < n:
            if nums[even_index] % 2 == 0:
                even_index += 2
            elif nums[odd_index] % 2 == 1:
                odd_index += 2
            else:
                # Swap out-of-place elements
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
                even_index += 2
                odd_index += 2

        return nums
