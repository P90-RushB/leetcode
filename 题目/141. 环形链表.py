# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 注意题意，只要判断是否是环形，
        # 不需要找到环形开头。
        # 双指针，一个指针每次走一步，另一个每次走两步，
        # 如果有环，一定会相遇。
        if not head or not head.next:
            return False

        i = j = head
        while i.next and j.next and j.next.next:
            # 这里需要注意的是，先把i，j执行next，再判断
            # 否则刚开始时就相等等于head。
            i = i.next 
            j = j.next.next
            
            if i == j:
                return True
        
        return False