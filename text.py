class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None
        root.next = None
        from collections import deque

        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop()
                if i != n-1:
                    node.next = q[0]
                else:
                    node.next = None
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root


s = Solution()
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
res = s.connect(node)
print(res)