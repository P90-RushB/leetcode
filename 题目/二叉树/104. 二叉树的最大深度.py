class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        # 方法零 我一直没想出来迭代咋写，主要是没想到咋同时记录深度…… 官方题解：
        # 栈里存元祖不就好了。
        # 迭代
        if not root:
            return 0
        stack = [(1, root)]
        max_len = 1
        
        while stack:
            deep, node = stack.pop()
            if node:
                max_len = max(max_len, deep)
                stack.append((deep+1, node.left))
                stack.append((deep+1, node.right))
        return max_len

        # 方法一，自顶向下
        # ans = 0
        # def help(node, depth):
        #     nonlocal ans
        #     if not node:
        #         return
        #     if not node.left and not node.right:
        #         ans = max(ans, depth)
        #     help(node.left, depth+1)
        #     help(node.right, depth+1)
        # help(root, 1)
        # return ans
        
        #  方法二，自底向上。
        if not root:
            return 0
        # 这段多余
        # if not root.left  and not root.right:
        #     return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    ########## 二刷写的 #######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归方式1，自底向上。
        # def helper(root, res):
        #     if not root:
        #         return res
        #     res += 1

        #     return max(helper(root.left, res), helper(root.right, res))
        # return helper(root, 0)

    # 递归2 自顶向下
        res = 0
        def helper(node, lv):
            nonlocal res
            if not node:
                return 
            res = max(res, lv)
            helper(node.left, lv+1)
            helper(node.right, lv+1)
        helper(root, 1)
        return res