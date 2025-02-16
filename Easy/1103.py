class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        nums = [0] * num_people  # Initialize the result list with zeros
        val = 1  # Start with the first candy to be given
        i = 0  # Start with the first person

        while candies > 0:
            if candies < val:
                nums[i] += candies
                break
            nums[i] += val
            candies -= val
            val += 1
            i = (i + 1) % num_people  # Move to the next person, wrap around if needed

        return nums
