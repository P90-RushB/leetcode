# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memo = {}
    def rob(self, root: TreeNode) -> int:

        ############ 方法一 暴力递归 #############
        # 先考虑如果暴力递归，怎么做
        # 在一个节点上，可以抢，也可以不抢；如果抢，下面两个就不能抢。
        # 如果当前节点不抢，就可以抢下两个。
        # 递归写法： 这个递归写法要想写出来，
        # 的精髓在于，边界条件定的要简单，就只判断当前节点是否是none,然后如果子节点存在，
        # 才递归子节点的子节点。
        # 边界条件：
        # if not root:
        #     return 0

        # # 如果当前节点抢：
        # rew1 = root.val
        # if root.left:
        #     rew1 += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     rew1 += self.rob(root.right.left) + self.rob(root.right.right)

        # # 如果当前节点不抢：
        # rew2 = self.rob(root.left) + self.rob(root.right)

        # return max(rew1, rew2)
        
    ############# 方法二 对方法一加备忘录 ################
        # if not root:
        #     return 0

        # ### 备忘录 ###
        # if root in self.memo:
        #     return self.memo[root]

        # # 如果当前节点抢：
        # rew1 = root.val
        # if root.left:
        #     rew1 += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     rew1 += self.rob(root.right.left) + self.rob(root.right.right)

        # # 如果当前节点不抢：
        # rew2 = self.rob(root.left) + self.rob(root.right)

        # self.memo[root] = max(rew1, rew2)
        # return self.memo[root]

    ############## 方法三 dp？ ##########
    # 这道题真的可以用dp，也就是自底向上的那种方式吗？理论上可以，但这是树，底
    # 就是左右节点，那首先得层序遍历，找到最后一层。再按照递归式，当成状态转移方程，
    # 进行自底向上，这太麻烦了。所以还是算了。

    ############## 方法四 还是递归，但状态不同了，这我竟然想到了
    ############## labuladong最后也是这种解法, 同时也是官方题解的思路 ##########
    # 在方法1 的递归中，状态是一维的，也就是：站在当前节点。
    # 可选的动作是：抢当前节点，或者不抢。 采取动作后，可能会转到子节点，
    # 也可能会转移到子节点的子节点（取决于当前节点抢还是不抢）。那当前状态
    # 其实就牵扯了后续两步的状态。
    # 而如果把状态定义成二维，状态：站在当前节点，且当前节点抢了，和站在当前
    # 节点，当前节点没抢。这样的二维状态下，如果当前节点下抢了，就会跳转到
    # 子节点状态下且子节点没抢； 如果当前节点下没抢，就可以跳转到子节点状态下抢，没抢都可以。
    # 这样就不会牵扯子节点的子节点。 labuladong 和官方也是这种思路。

    ##################### 但是 #####################
    # 这种方式真的就够了吗？够好了吗？  错。
    # 与方法一 状态 + 动作 进行转移 相比， 这里用状态之间的转移，但优化幅度并没有那么大，
    # 所优化的地方其实是，当把动作变成第二维状态后，例如，站在当前节点下且抢了，那么左右孩子
    # 节点一定不能抢，确定性的转移，一定程度减少了计算量。但只是一定程度。可能大家都没有意识到，
    # 虽然数组名字用的dp，但这种方式还是暴力递归，只不过状态的定义巧妙了。
    # 重复计算的地方在于：如果站在当前节点下且抢了，子节点不能抢； 如果站在当前节点下且没抢，下个节点可以
    # 抢可以不抢， 下个节点不抢，计算了两次。 

# 二维状态，不加备忘录下， 超时
        # def helper(root):
        #     if not root:
        #         return [0, 0]
            
        #     dp = [0, 0]
        #     # 如果当前节点下抢了
        #     dp[0] = root.val + helper(root.left)[1] + helper(root.right)[1]
        #     # 如果当前节点下没抢
        #     dp[1] = max(helper(root.left)) + max(helper(root.right))
        #     return dp
        # return max(helper(root))

# 二维状态下，加备忘录，过了。 这里字典存储的意思是 当前节点下且不抢，最大收益。
        def helper(root):
            if not root:
                return [0, 0]
            
            dp = [0, 0]
            # 如果当前节点下抢了
            dp[0] = root.val + helper(root.left)[1] + helper(root.right)[1]
            # 如果当前节点下没抢
            if root not in self.memo:
                self.memo[root] = max(helper(root.left)) + max(helper(root.right))
            dp[1] = self.memo[root]
            return dp
        return max(helper(root))


# 但可能真的不需要备忘录………… 评论区还是用这种思想， 但编写方式稍微变了下，好像很高效。
# 好像就没有重复计算了，之后再搞清楚。
        # def _rob(root):
        #     if not root: return 0, 0
            
        #     ls, ln = _rob(root.left)
        #     rs, rn = _rob(root.right)
            
        #     return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        # return max(_rob(root))