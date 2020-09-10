class MinStack:
# 很简单，多一个辅助栈，存对应时刻的当前最小元素。弹出的时候同时判断下最小元素栈是否该弹出元素。
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.s_min = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.s_min) == 0 or self.s_min[-1] >= x:
            self.s_min.append(x)

    def pop(self) -> None:
        if len(self.s):
            if self.s_min[-1] == self.s[-1]:
                self.s_min.pop()
            self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_min[-1]