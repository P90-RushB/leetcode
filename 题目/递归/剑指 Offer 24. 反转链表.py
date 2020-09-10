# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 方法1， 递归
        # if not head or not head.next:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        # 方法2， 迭代，用双指针
        cur = None
        pre = head
        while pre:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
        return cur

        # 最后，我写的麻烦的迭代双指针，因为while写的不好，不应该判断next
        # 否则就要在while之后多判断，麻烦了。
        # if not head:
        #     return None

        # tmp1 = None
        # tmp2 = head
        # while tmp2 and tmp2.next:
        #     tmp3 = tmp2.next
        #     tmp2.next = tmp1
            
        #     tmp1 = tmp2
        #     tmp2 = tmp3

        # tmp2.next = tmp1

        # return tmp2

            