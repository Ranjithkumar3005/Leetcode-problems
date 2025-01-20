# The rand7() API is already defined for you.
def rand7():
    # @return a random integer in the range 1 to 7
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number in the range [1, 49]
            num = (rand7() - 1) * 7 + rand7()
            # Accept only numbers in the range [1, 40]
            if num <= 40:
                # Map [1, 40] uniformly to [1, 10]
                return 1 + (num - 1) % 10
