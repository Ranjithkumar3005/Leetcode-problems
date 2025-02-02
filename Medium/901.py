class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.st == [] or self.st[len(self.st) - 1][0] > price:
            self.st.append([price, 1])
            return 1
        else:
            tem = 0
            while self.st != [] and self.st[len(self.st) - 1][0] <= price:
                tem += self.st[len(self.st) - 1][1]
                self.st.pop()
            self.st.append([price, tem + 1])
            return tem + 1
