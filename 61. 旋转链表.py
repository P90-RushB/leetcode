# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 看懂旋转的本质就简单了。旋转一位，就是最后面的数往前扔一个。那旋转k位，就找倒数第k个数，
        # 就是链表的新的开头
        if not head or not head.next:
            return head
        
        cnt = 0
        tmp = head

        # 统计一下有多少个
        while tmp:
            cnt += 1
            tmp = tmp.next

        # 如果是k整数倍，那就不用旋转。
        k = k % cnt
        if k == 0:
            return head

        # 找倒数第 k + 1 个数，（第k+1个数是链表新的结尾）
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next 
            fast = fast.next
        
        res =slow.next
        fast.next = head
        slow.next = None
        return res