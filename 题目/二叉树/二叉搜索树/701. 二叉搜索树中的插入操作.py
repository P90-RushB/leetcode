# 简单递归  方法一 我的写法：
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            if not root.left:
                root.left = TreeNode(val)
                return root
            self.insertIntoBST(root.left, val)
        
        else:
            if not root.right:
                root.right = TreeNode(val)
                return root
            self.insertIntoBST(root.right, val)

        return root

# 方法二，迭代形式。方法一我的递归和这种迭代极其相似。
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)

# 方法三， 官方题解更简洁的递归。如果用递归，下面这种代码要少的多。
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root