# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 从跟开始，如果pq在根节点两侧，那根就是最近公共。如果在一侧，递归；
        # 如果遇到p或q，那p或q就是
        if not root:
            return
        a = root.val - p.val
        b = root.val - q.val
        if a == 0:
            return root.val
        if b == 0:
            return root.val
        if a < 0 and b < 0:
            return self.lowestCommonAncestor(root.right, p, q)
        if a > 0 and b > 0:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

s = Solution()
node = TreeNode(6)
node.left = TreeNode(2)
node.right = TreeNode(8)
node.left.left = TreeNode(0)
node.left.right = TreeNode(4)
node.right.left = TreeNode(7)
node.right.right = TreeNode(9)
node.left.right.left = TreeNode(3)
node.left.right.right = TreeNode(5)
res = s.lowestCommonAncestor(node, TreeNode(2), TreeNode(8))
print(res)
