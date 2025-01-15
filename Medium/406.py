class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        # Insert each person into the queue based on their k value
        for person in people:
            queue.insert(person[1], person)

        return queue
