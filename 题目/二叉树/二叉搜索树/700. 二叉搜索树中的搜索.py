# 简单递归
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        # 方法1， 迭代
        if not root:
            return None
        p = root
        while p:
            if p.val == val:
                return p
            elif p.val < val:
                p = p.right
            else:
                p = p.left
        return None
    
        # 方法2， 递归
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) if root.val > val else \
            self.searchBST(root.right, val)