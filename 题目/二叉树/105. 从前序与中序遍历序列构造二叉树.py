class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 由前序和中序构造二叉树。其思路和 106题 由后序和中序构造二叉树一毛一样。
        # 题解看106的官方题解。
        # 同理，需要注意的是，该题中要先赋值 root.left , 再 root.right
        # 因为在前序中，拿掉第一个元素（根）之后，新的第一个元素，代表左子树的根。
        def help(left, right):
            if left > right:
                return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            idx = dic[val]
            root.left = help(left, idx-1)
            root.right = help(idx+1, right)
            return root
        
        dic = {v:k for k,v in enumerate(inorder)}
        return help(0, len(inorder)-1)

# 我写的方法二，套路和106一样，我的这个写法，优化的地方是：不应该用顺序遍历，而是哈希表存储中序的索引。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        # 从先序里找到根
        root = TreeNode(preorder.pop(0))

        # 从中序里遍历，找到根的左子树的最后一个数。
        left = []
        right = []
        left_idx = -float('inf')

        for k,v in enumerate(inorder):
            if v != root.val:
                left_idx = k
            else:
                break

        if left_idx == -float('inf'):     
            left = []
            right = inorder[1:]
        else:
            left = inorder[:left_idx+1]
            right = inorder[left_idx+2:] if left_idx+2 < len(inorder) else []

        pre_left =  preorder[: len(left)] if left else []
        pre_right = preorder[len(pre_left):] if right else []
        root.left = self.buildTree(pre_left, left)
        root.right = self.buildTree(pre_right, right)

        return root