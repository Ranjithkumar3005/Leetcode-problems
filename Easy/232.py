class MyQueue:

    def __init__(self):
        self.stack = []
        self.q = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.q) == 0:
            self._prep()

        return self.q.pop()

    def peek(self) -> int:
        if len(self.q) == 0:
            self._prep()

        return self.q[-1]

    def _prep(self):
        while self.stack:
            self.q.append(self.stack.pop())

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
