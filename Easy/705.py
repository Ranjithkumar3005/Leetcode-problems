class MyHashSet(object):

    def __init__(self):
        self.h = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.h[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.h:
            self.h.pop(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.h:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
