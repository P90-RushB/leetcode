class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 从中序和后序来构造二叉树。 看的leetcode的官方题解。
        # 思路还是很清晰的，需要格外注意的是，要先赋值root.right,再赋值root.left.
        # 因为后序遍历的顺序是左右根。意味着，拿掉一个根（后序的最后一个数后），后序中新的最后一个数，
        # 是原树根节点的right子节点，也就是右子树的根。

        def helper(in_left, in_right):
            # 如果没有构建子树的元素：
            if in_left > in_right:
                return None
            
            # 后序的最后一个节点是根。
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            # 从根的位置，把中序数组分成左右子树
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)


# 二刷时我自己写的，长了点，不过思路和官方题解（方法一）一样，比较清晰：
# 我的这个思路是，从后序中读一个根之后，找到根在中序中的位置（目前是顺序遍历来找的，这样非常低效，
# 可以改成哈希表存储中序索引， 知道就行了，懒得改了。 要这样改的话，整个逻辑要写到helper函数里，字典写到helper外面），
# 然后先把中序按根分成左右两个数组，然后既然已经知道了左边数组的长度L，后续中的左子树 left_post
# 其实就是后序中的前L个数。就可以把后序也分成左右两个数组，然后，就递归。
# 注意，方法一与我的方法本质上一样，看起来有区别，仅仅是因为，我对中序和后序都分成左右数组，而方法一利用了一条性质：
# 后序的倒数第二个节点是右子树的根，利用这个性质，方法一没有 将后序也分成两个数组，同时，必须先遍历右子树，再遍历左子树，
# 这样对后序数组倒着来，递归解决。
class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        # 从后序里找到根
        root = TreeNode(postorder.pop())

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

        post_left =  postorder[0: len(left)] if left else []
        post_right = postorder[len(post_left):] if right else []
        root.left = self.buildTree(left, post_left)
        root.right = self.buildTree(right, post_right)

        return root