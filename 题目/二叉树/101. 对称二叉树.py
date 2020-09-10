
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 方法一，递归
#         if not root:
#             return True
        
#         def help(node1, node2):
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
            
#             return help(node1.left, node2.right) and help(node1.right, node2.left)
#         return help(root.left, root.right)
    
    # 方法二： 层序遍历。 用栈
        if not root:
            return True

        cur = [root]
        post = []
        layer_val = []
        while cur:
            for i in cur:
                if i.left:
                    post.append(i.left)
                    layer_val.append(i.left.val)
                else:
                    layer_val.append(None)
                if i.right:
                    post.append(i.right)
                    layer_val.append(i.right.val)
                else:
                    layer_val.append(None)
                
            if layer_val:
                n = len(layer_val)
                idx1, idx2 = 0, n-1
                while idx2 > idx1:
                    if layer_val[idx1] != layer_val[idx2]:
                        return False
                    idx2 -= 1
                    idx1 += 1
            layer_val = []
            cur = post
            post = []
        return True

    # 方法三 官方题解的层序遍历，写的很精简，将树复制一份，每次入队第一棵树的一个节点，和第二个数的对称节点，这样就好比较了。        # 迭代，层序遍历，用队列。
        # 因为这题判断对称，不需要每层一个list，这样就是标准的队列实现层序，写起来简单的多。
        if not root:
            return True

        from collections import deque
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            a = q.pop()
            b = q.pop()
            if (a!=None) ^ (b!=None):
                return False
            if not a and not b:
                continue
            if a.val != b.val:
                return False
            q.append(a.left)
            q.append(b.right)
            q.append(a.right)
            q.append(b.left)
        return True