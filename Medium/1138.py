class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        # Calculate the positions of each character on the board
        pos = {c: (i // 5, i % 5) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}

        x, y = 0, 0  # Starting position at 'a' (0, 0)
        result = ""

        for char in target:
            new_x, new_y = pos[char]  # Target position

            # Move left or up first to handle the special case of 'z'
            if new_y < y:
                result += "L" * (y - new_y)
            if new_x < x:
                result += "U" * (x - new_x)

            # Move right or down
            if new_y > y:
                result += "R" * (new_y - y)
            if new_x > x:
                result += "D" * (new_x - x)

            # Add the '!' to indicate reaching the target character
            result += "!"

            # Update current position
            x, y = new_x, new_y

        return result
