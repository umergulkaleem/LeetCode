class MyStack:

    def __init__(self):
        self.fakestack = deque()

    def push(self, x: int) -> None:
        self.fakestack.append(x)
        

    def pop(self) -> int:
        tmp = []
        last = len(self.fakestack)-1
        for i in range(len(self.fakestack)):
            curr = self.fakestack.popleft()
            if i != last:
                self.fakestack.append(curr)
        return curr

    def top(self) -> int:
        tmp = []
        last = len(self.fakestack)-1
        for i in range(len(self.fakestack)):
            curr = self.fakestack.popleft()
            if i != last:
                self.fakestack.append(curr)
        self.fakestack.append(curr)
        return curr
        

    def empty(self) -> bool:
        if len(self.fakestack) == 0:
            return  True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()