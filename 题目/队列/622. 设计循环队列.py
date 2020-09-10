# 其实就是这么简单……  我写的和官方题解一毛一样。
# 只需要start索引和有效数组长度size，end索引就可以推出来。
# 我的体会和官方题解的说法一样：能推出来就尽量不要多加变量（说的就是end），多维护一个变量就多了很多操作，
# 更加容易错。 end索引 = （start索引 + size -1） % max_size
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k
        self.max_size = k
        self.start = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[(self.start + self.size) % self.max_size] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.start]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.start + (self.size-1)) % self.max_size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.max_size