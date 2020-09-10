# 简单递归
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) if root.val > val else \
            self.searchBST(root.right, val)