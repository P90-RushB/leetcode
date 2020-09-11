# 这题虽然长，思路是很清晰的，也很经典。
# 下面是leetcode的官方题解的代码，难得写的很好。
# 详细解释可以看官方题解。

class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

# 按照官方思路，自己写的，基本一毛一样。
class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
             return 

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # root.val == val

            # 叶节点直接删除
            if not root.left and not root.right :
                return 
            # 先不管有没有左子节点，如果有右节点，
            # 那就找root的后继节点（中序遍历顺序中的下个节点），找法也简单：
            # 先右，然后一路左走。这里写在 successor函数里。
            elif root.right:
                succ = self.successor(root)
                root.val = succ.val
                # 当前节点的值已经被替换成了后继节点的值，
                # 相当于已经用后继节点替换了当前节点了；但其实后继并没有删除，
                # 要做的其实是在root.right 为根的子树中，删除succ节点，
                # 这就递归上了。
                root.right = self.deleteNode(root.right, succ.val)
            
            else: # 说明右节点不存在，左节点存在。
            # 那就找root的前驱节点，也就是左子树，然后一路找最右。
            # 该逻辑写在 predcessor函数里
                pred = self.predecessor(root)
                root.val = pred.val
                # 在root.left为根的树中删除pred节点，这就递归上了。
                root.left = self.deleteNode(root.left, pred.val)

        return root

