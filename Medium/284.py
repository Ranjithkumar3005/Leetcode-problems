# Assuming the Iterator class is already implemented
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = None  # This will hold the "peeked" element
        self.has_peeked = False  # This tells us if there's a peeked element

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_peeked:
            if self.iterator.hasNext():
                self.buffer = self.iterator.next()
                self.has_peeked = True
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        if self.has_peeked:
            result = self.buffer
            self.buffer = None
            self.has_peeked = False
            return result
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_peeked or self.iterator.hasNext()


# Example usage:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     print(val)          # Use the peeked value.
#     iter.next()         # Move the iterator to the next element.
