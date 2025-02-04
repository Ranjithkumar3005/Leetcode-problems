class RecentCounter(object):
    def __init__(self):
        """
        Initializes the RecentCounter with an empty list to keep track of requests.
        """
        self.requests = []

    def ping(self, t):
        """
        Adds a new request at time t and returns the number of requests that have happened in the past 3000 milliseconds (inclusive of the new request).

        :type t: int
        :rtype: int
        """
        # Add the new request time to the list
        self.requests.append(t)

        # Remove requests that are outside the 3000 milliseconds window
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)

        # Return the number of requests within the time window
        return len(self.requests)
