# 我写的，结构上不够好，最好看官方题解。

class ListNode:
    def __init__(self, val):
        self.val = val
        self.pre = self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = ListNode(-1)
        self.cnt = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index + 1 >self.cnt:
            return -1

        tmp = self.dummy
        for i in range(index+1):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = ListNode(val)
        
        tmp1 = self.dummy
        while tmp1 and tmp1.next:
            tmp1 = tmp1.next
        tmp1.next = tmp
        tmp.pre = tmp1
        self.cnt += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 按题目要求，如果索引大于链表长度，不添加
        if index > self.cnt:
            return
        if index == self.cnt:
            # 插到末尾
            self.addAtTail(val)

        else:
            tmp = self.dummy
            if index < 0:
                index = 0
            for _ in range(index):
                tmp = tmp.next
            new = ListNode(val)
            new.pre = tmp
            new.next = tmp.next

            tmp.next = new
            new.next.pre = new

            self.cnt += 1

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.cnt-1:
            return 
        tmp = self.dummy
        for _ in range(index):
            tmp = tmp.next
        if index == self.cnt - 1:
            tmp.next = None
        else:
            tmp.next = tmp.next.next
            if tmp.next:
                tmp.next.pre = tmp
        self.cnt -= 1