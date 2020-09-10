# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 分治经典题，还要仔细琢磨
    def generateTrees(self, n: int) -> List[TreeNode]:
        res = []
        if n == 0:
            return res

        # 看博客分析。
        # 这是分治的思想，遍历每个节点，每个节点i都当一次整棵树的根节点
        # 当i作为根节点时，小于i的都在左子树，大于i的都在右子树。
        # 递归调用，对于左子树，遍历每个节点，作为左子树的根节点，右子树也一样
        # ...

        def helper(start, end):
            if start > end: return [None]
            res = []
            for i in range(start, end+1):
                left = helper(start, i-1)
                right = helper(i+1, end)
                for j in left:
                    for k in right:
                        node = TreeNode(i)
                        node.left = j
                        node.right = k
                        res.append(node)
            return res

        return helper(1, n)

