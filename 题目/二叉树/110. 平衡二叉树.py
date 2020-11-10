# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 方法1，on2复杂度，绝对不能用：
        # 自顶向下递归。首先写个求当前节点高度的函数。
        # 遍历二叉树，如果节点左右子树高度不超过一说明满足。
        # def helper(node):
        #     if not node:
        #         return 0
        #     return max(helper(node.left), helper(node.right)) + 1
        
        # if not root:
        #     return True
        # if abs(helper(root.left) - helper(root.right)) > 1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)

        # 方法2， 自底向上,helper返回当前节点高度。
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return helper(root) >= 0