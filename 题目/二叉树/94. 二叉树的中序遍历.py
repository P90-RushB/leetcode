# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def help(node):
            nonlocal res
            if not node:
                return 
            help(node.left)
            res.append(node.val)
            help(node.right)
        help(root)
        return res

# 迭代
