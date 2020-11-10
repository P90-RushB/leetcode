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

##################################################################
# 按照官方思路，我写的，强烈推荐看这个。

class Solution:
        
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 方法：递归到目标节点，如果目标节点是
        #   1. 叶节点，直接删除就好了
        # （这里要注意的是，因为是递归，所以能够在这一层里返回None，栈的前一层是
        # node.left或者node.right = 该层返回值（None）,从而直接删除了叶节点。如果是
        # 迭代，只知道当前叶节点，当然没法从树里删除，因为要node.parent.子节点 = None 需要
        # 知道父节点。这题不能用迭代）
        #   注意. 按正常逻辑，情况1之后（叶节点），下面的情况应该是：
        #   只有左，只有右， 左右都有， 三种情况。但！！！！ 为了代码方便，
        #   实际上按顺序，情况写成了：有右节点， 无右节点两种情况。这个要记住。
        #  2. 有右节点。有右节点，就能够找到逻辑后继。用逻辑后继的值替代当前值，
        #   然后对node.right为根的这个数，删除逻辑后继的值，这就形成了递归。
        #   3. 没有右节点，只有左节点，那就找逻辑前驱，然后用逻辑前驱的值期待当前值，
        #   并对node.left为根的树，产出逻辑前驱的值，这就形成了递归。

        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # 否则，找到目标值。
        # 情况1，是叶节点
        if not root.left and not root.right:
            return None
        # 情况2，有右节点
        if root.right:
            root.val = self.successor(root)
            root.right = self.deleteNode(root.right, root.val)

        # 情况3， 没有右，只有左。
        else:
            root.val = self.predecessor(root)
            root.left = self.deleteNode(root.left, root.val)
        return root
