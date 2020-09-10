class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 这题不容易理解。看leetcode 题解 Krahets这个大佬的解释，比较清楚。
        # 按照思路，自己拿例子脑子跑一下。
        # 整体是后序，这样保证找到的是最近（最深）公共祖先。


        # 解析：
        #   终止条件：
                # 当越过叶节点，则直接返回 None ；
                # 当 root 等于 p或q，则直接返回 root

        #   递推工作：
                # 开启递归左子节点，返回值记为 left ；
                # 开启递归右子节点，返回值记为 right；
        # 四种情况：
            # 返回值： 根据 leftleft 和 rightright ，可展开为四种情况；
            #     1.当 left 和 right同时为空 ：说明 root的左 / 右子树中都不包含 p,q，返回 None；
            #     2.当 left和 right 同时不为空 ：说明 p, q分列在 rootroot 的异侧 （分别在 左 / 右子树），
            #       因此 root为最近公共祖先，返回 root
            #     3.当 left为空 ，right不为空 ：p,q都不在 root的左子树中，直接返回 right。
            #       具体可分为两种情况：
            #         p,q其中一个在 root的 右子树 中，此时 right指向 p（假设为 p）；
            #         p,q两节点都在 root的 右子树 中，此时的 right指向 最近公共祖先节点 ；
            #     4.当 left不为空 ， right为空 ：与情况 3. 同理；


        # 四种情况分开的详细版本：
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right:

        # 将几种情况能合并的合并后的版本：
        # if not root or root == p or root == q: return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if not left: return right
        # if not right: return left
        # return root