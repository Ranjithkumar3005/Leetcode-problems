class MyStack(object):

    def __init__(self):
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)

    def pop(self):
        """
        :rtype: int
        """
        dum = self.st[len(self.st) - 1]
        self.st.pop()
        return dum

    def top(self):
        """
        :rtype: int
        """
        return self.st[len(self.st) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        print(self.st)
        if len(self.st) == 0:
            return True
        else:
            return False
