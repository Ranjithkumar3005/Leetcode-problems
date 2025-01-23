class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.que = []
        self.k = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.que) != self.k:
            self.que.insert(0, value)
            return True
        return False

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.que) != self.k:
            self.que.append(value)
            return True
        return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.que) != 0:
            self.que.remove(self.que[0])
            return True
        return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.que) != 0:
            self.que.pop()
            return True
        return False

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.que) == 0:
            return -1
        return self.que[0]

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.que) == 0:
            return -1
        return self.que[len(self.que) - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.que == []:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.que) == self.k:
            return True
        return False
