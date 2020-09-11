根据二叉搜索树性质，简单递归。
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 从跟开始，如果pq在根节点两侧，那根就是最近公共。如果在一侧，递归；
        # 如果遇到p或q，那p或q就是
        if not root:
            return
        a = root.val - p.val
        b = root.val - q.val
        if a == 0 or b == 0:
            return root
        if a < 0 and b < 0:
            return self.lowestCommonAncestor(root.right, p, q)
        if a > 0 and b > 0:
            return self.lowestCommonAncestor(root.left, p, q)
        return root