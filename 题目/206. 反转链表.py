# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        pre = None
        now = head

        while now:
            # 获取now的下个节点，临时保存
            tmp = now.next
            # 翻转的核心，就一句：当前节点的next为pre，就把俩节点间的线翻转了，每次循环其实
            # 就做了这一件事
            now.next = pre
            
            # pre和now都右挪一下。
            pre = now
            now = tmp

        return pre

        # 迭代2，我写的垃圾思路，太麻烦了

        # 我写的，结果没问题，但思路没问题，搞得太麻烦了……
        # 应该： 不保存什么开头，遍历，每次，只是改变一个箭头方向而已，这才是反转链表精髓。

        # 我的烂方法：
        # 递归需要 头结点head， 当前节点now（当前要扔到现在的头结点之前的节点）， 和now的前一个节点pre
        # 操作是：pre.next = now.next, now.next = head, head = now
        # 终止条件，now已经成None了，不用扔到前面了。
        # def helper(head, pre, now):
        #     if not now:
        #         return head

        #     pre.next = now.next
        #     now.next = head
        #     head = now

        #     now = pre.next

        #     head = helper(head, pre, now)

        #     return head
        
        # if not head:
        #     return None
        # if not head.next:
        #     return head
        # return helper(head, head, head.next)

        # 方法2 递归

        if not head or not head.next:
            return head
        # 递归到最深处，p等于最后一个节点，也就是新链表的头节点，然后不断将其出栈，最后返回该节点。相当于后序遍历，子逻辑处理完，开始将当前节点反着链接
        p = self.reverseList(head.next)
        head.next.next = head
        # 下一次出栈时，会更新这个head.next为前一个节点，到最后，只有老的最头的节点的next为None
        head.next = None
        return p



