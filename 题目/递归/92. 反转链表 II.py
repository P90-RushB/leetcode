class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # labuladong有专题。 这题挺难的，细节不少
        # 思路，可以先解决反转前k个位置的链表的问题，
        # 再解决从m到n位置反转的链表

        # successor用来保持第k+1个节点，用来连接成完整的链表
        successor =  None
        def reverseK(head, k):
            nonlocal successor
            # 反转前k个节点的写法，和反转整个链表的写法大部分相同。
            # k == 1,是只有自己的情况
            if k == 1:
                successor = head.next
                return head

            new_head = reverseK(head.next, k-1)
            head.next.next = head
            head.next = successor
            return new_head


        if m == 1:
            head = reverseK(head, n)
        else:
            head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

        