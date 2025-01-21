class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []

        # Traverse nums2 to compute next greater elements
        for num in nums2:
            # While stack is not empty and the current number is greater than the stack's top
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)

        # For any numbers left in the stack, there is no next greater element
        while stack:
            smaller_num = stack.pop()
            next_greater[smaller_num] = -1

        # Map the results to nums1
        return [next_greater[num] for num in nums1]
