验证一个二叉树是否是二叉搜索树，
性质：一个节点左子树所有节点都小于该节点；
    右子树所有节点都大于该节点。

第一眼看，会觉得很简单，可以中序遍历看是否是递增序列即可求解。
但 假如 二叉搜索树是可以 左<=根<右，那么就不行了，因为中序遍历，并不区分左右。

这时，就只能用另一种方法：根绝二叉搜索树本身的性质，但不是那种直接和左右孩子比的递归，因为
那样实际上并不符合二叉搜索树，
具体：https://github.com/labuladong/fucking-algorithm/blob/master/数据结构系列/二叉搜索树操作集锦.md
正确的做法是：使用辅助函数，增加函数参数列表，在参数中携带额外信息

也就是下面的方法1，这种递归不太好想。首先，根大于无穷小，小于无穷大，这不是废话吗？并不是。
递归遍历了所有节点，每遍历到一个节点，都会修改min和max这俩边界，使得能够判断
比如root.left.val,要小于root.val，而root.left.right时，root.val作为max限制了其上限，root.left.val作为
min，限制了其下限,就是这样递归的。

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # 方法1，这道题最合适的解法。不使用中序的性质。
        # 因为，如果题目要求 左<=根 < 右，那么中序遍历无法区分左右，就无法检验二叉搜索树了
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