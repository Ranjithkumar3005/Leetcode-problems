class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []  # To store the fully justified lines
        current_line = []  # To hold the current line of words
        current_length = 0  # Current line length without spaces

        for word in words:
            # Check if adding the new word exceeds maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # If it does, justify the current line
                for i in range(maxWidth - current_length):
                    # Distribute spaces evenly between the words
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                # Add the justified line to the result
                result.append("".join(current_line))
                # Reset current line and length
                current_line, current_length = [], 0
            # Add the current word to the line
            current_line.append(word)
            # Update the length
            current_length += len(word)

        # Handle the last line (left-justified)
        result.append(" ".join(current_line).ljust(maxWidth))

        return result
