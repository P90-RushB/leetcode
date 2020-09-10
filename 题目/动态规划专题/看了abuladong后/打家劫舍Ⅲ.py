# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 在根节点处 这个状态下的 可偷最高金额，
        # 等于 max(root.val + max(v(root.left.left), v(root.left.right)),
        # root.val + max(v.root.right.left), v.root.right.right), v.root.left, v.root.right)
        dic = {}
        def value(node):
            if not node:
                return 0
                
            if node in dic:
                return dic[node]

            if not node.left and not node.right:
                dic[node] = node.val
                return node.val

            v1 = value(node.left)
            v2 = value(node.right)
            
            v3, v4 = 0, 0
            if node.left:
                v3 =  value(node.left.left) + value(node.left.right)

            if node.right:
                v4 = value(node.right.left) + value(node.right.right)
            res = max(v1+v2, node.val + v3 + v4)
            dic[node] = res
            return res
        return value(root)