# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # 方法1，这道题最合适的解法。不使用中序的性质。
        # 因为，如果题目要求 左<=根 < 右，那么中序遍历无法区分左右，就无法检验二叉搜索树了

        # 这个递归为啥不好想吧，因为我一直想着bst的性质，根要大于左子树所有节点，小于右子树所有节点，
        # 所以很自然的会想到，对于每个根，判断是否大于左子树的max值，小于右子树的min值，这样逻辑当然没错，但写起来很头疼。

        # 而下面这种正确解法，不是对每个根判断是否符合，而是从根开始，范围是负无穷到正无穷，那第一个根肯定符合，而递归限定（改变）的是
        # 左右子树的范围，这样不断限定后面的范围。 先序遍历。
        min_v = -float('inf')
        max_v = float('inf')
        def check(node, min_v, max_v):
            if not node:
                return True
            if min_v >= node.val or node.val >= max_v:
                return False

            return check(node.left, min_v, node.val) and \
             check(node.right, node.val, max_v)

        return check(root, min_v, max_v)

        # # 方法2，中序遍历,判断数组是否递增
        # if not root:
        #     return True
        # li = []

        # def inorder(node):
        #     if not node:
        #         return             
        #     inorder(node.left)
        #     li.append(node.val)
        #     inorder(node.right)

        # inorder(root)

        # for i in range(1, len(li)):
        #     if li[i] <= li[i-1]:
        #         return False
        # return True

        # 方法3，对方法一优化，不建立整个数组，只判断相邻元素是否递增。
        # pre_v = None
        # def inorder(node):
        #     nonlocal pre_v
        #     if not node:
        #         return True
        #     if not inorder(node.left):
        #         return False
        #     if pre_v !=None and pre_v >= node.val:
        #         return False
        #     else:
        #         pre_v = node.val

        #     return inorder(node.right)
        # return inorder(root)