class MyQueue:

    # def __init__(self):
    #     self.fakequeue = []
        

    # def push(self, x: int) -> None:
    #     self.fakequeue.append(x)

    # def pop(self) -> int:
    #     # last = len(self.fakequeue)

    #     # for i in range(len(self.fakequeue)):
    #     #     curr = self.fakequeue.pop()
    #     #     if i != last:
    #     #         self.fakequeue.append(curr)
        
    #     # return curr
        

    #     # last = len(self.fakequeue)
    #     first = 0

    #     for i in range(len(self.fakequeue)):
    #         curr = self.fakequeue.pop()
    #         print(self.fakequeue,"after pop removed",curr)
    #         if i != first:
    #             self.fakequeue.append(curr)
    #     print(curr,"end")
    #     return curr

    #     # curr = self.fakequeue.pop()
    #     # return curr
    # def peek(self) -> int:
    #     first = len(self.fakequeue)-1
    #     mynumber = 0
    #     for i in range(len(self.fakequeue)):
    #         curr = self.fakequeue.pop()
    #         print(self.fakequeue,"after pop removed",curr)
    #         if i == first:
    #             mynumber = curr
    #         self.fakequeue.append(curr)
    #     print(curr,"end")
    #     return mynumber
        

    # def empty(self) -> bool:
    #     return len(self.fakequeue) == 0


    def __init__(self):
        self.fakequeue = []
        self.second = []

    def push(self, x: int) -> None:
        self.fakequeue.append(x)

    def pop(self) -> int:
        if not self.second:
            while self.fakequeue:
                curr = self.fakequeue.pop()
                self.second.append(curr)

        return self.second.pop()

    def peek(self) -> int:
        if not self.second:
            while self.fakequeue:
                curr = self.fakequeue.pop()
                self.second.append(curr)

        return self.second[-1]

    def empty(self) -> bool:
        return len(self.fakequeue) == 0 and len(self.second) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()