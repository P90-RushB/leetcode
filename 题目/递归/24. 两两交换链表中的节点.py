# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归最简单
        if not head or not head.next:
            return head

        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        head = tmp

        head.next.next = self.swapPairs(head.next.next)
        
        return head

# 官方题解的递归写的精炼些，一样的：
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

# 方法2， 迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 迭代
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:
            one = tmp.next
            two = tmp.next.next

            tmp.next = two
            tmp1 = two.next
            two.next = one
            one.next = tmp1

            tmp = tmp.next.next

        return dummy.next


