class MyCalendar(object):

    def __init__(self):
        self.dum = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for booking in self.dum:
            # Check if the new booking overlaps with any existing booking
            if not (end <= booking[0] or start >= booking[1]):
                return False
        # If no overlap, add the booking and return True
        self.dum.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start, end)
