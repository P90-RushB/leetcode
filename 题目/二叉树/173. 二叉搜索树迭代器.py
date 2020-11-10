# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 用迭代的方式来中序遍历，就是受控递归，可以控制空间复杂度，
# 因为中间可以停顿，每次停顿在左子树为空的地方。
class BSTIterator:

    def __init__(self, root: TreeNode):
        # 开局建栈，并调用_stak_left,从根一路压栈到左子树为空。这时，
        # 栈顶就是最小的数（二叉搜索树是中序遍历有序的）
        # self.stack = []
        # self._stack_left(TreeNode)

        self.stack = []
        self._stack_left(root)


    def _stack_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmp = self.stack.pop()
        if tmp.right:
            self._stack_left(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()