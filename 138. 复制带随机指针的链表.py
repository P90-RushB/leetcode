"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# 这是我写的，其实就是普通的遍历。 官方题解爹方法1用的递归，没仔细看，我没想到递归怎么做。
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
        orig = head

        dummy = tmp = Node(-1)
        while orig:
            tmp.next = Node(orig.val)
            tmp = tmp.next
            orig = orig.next
        
        tmp = dummy.next
        orig = head
        
        while orig:
            if not orig.random:
                orig = orig.next
                tmp = tmp.next
                continue
            
            target = orig.random
            tmp_tmp = head
            tmp_tmp1 = dummy.next
            while tmp_tmp:
                if tmp_tmp == target:
                    tmp.random = tmp_tmp1
                    break
                tmp_tmp = tmp_tmp.next
                tmp_tmp1 = tmp_tmp1.next

            orig = orig.next
            tmp = tmp.next

        return dummy.next