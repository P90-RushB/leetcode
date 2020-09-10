# 认真看，果然还是看的懂，懂了发现……也不难
# https://github.com/labuladong/fucking-algorithm/blob/master/动态规划系列/编辑距离.md

# 首先，思考如何暴力递归：
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 定义i j从两个字符串末尾超前走，其实很好理解
        # 要把第一个字符串变成第二个字符串，对每个i，所有能做的操作就4个：
        # 如果i等于j，两个索引都左移就行。如果不等，那可以对i进行三种可能的
        # 操作：插入，替换，删除。 遍历，这种暴力递归，肯定是可以算出正确答案的。

        # dp定义， dp[i,j] 表示word1[0-i]与word2[0-j]之间的编辑距离
        # 可见，状态是二维的
        # 递归边界： 当i走到头了，这时对于第二个字符串的0-j个字符，只能插入了
        #           当j走到头了，这时对于第一个字符串剩下的0-一个字符，都删了就完了

        def dp(i, j):
            if i == -1:
                # 那只能插入了
                return j + 1
            elif j == -1:
                # 那只能删除了
                return i + 1
            elif word1[i] == word2[j]:
                return dp(i-1, j-1)
            else:
            # 分别对应：删了i， i位置插了j的字母， 
                return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1

        return dp(len(word1) - 1, len(word2) - 1)

# 在写出上面的暴力递归之前，我根本不知道怎么用动归来做。但一旦暴力递归写出来了，
# 看上面的  return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1 ，
# dp[i, j]只依赖（i-1, j）, (i, j-1), (i-1, j-1) 三个状态，这动归不就出来了。

# 下面先不用动归，用递归加备忘录来写一下方法二
# 然而，备忘录也超时了……
        # 方法二 递归加备忘录
        dic = {}
        def dp(i, j):
            if i == -1:
                # 那只能插入了
                return j + 1
            elif j == -1:
                # 那只能删除了
                return i + 1
            elif word1[i] == word2[j]:
                if (i, j) not in dic:
                    dic[(i, j)] = dp(i-1, j-1)
                return dic[(i,j)]
            else:
                if (i, j) not in dic:
                    dic[(i, j)] = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
                return dic[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


# 方法三 dp，有了方法一暴力递归的 return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1 
# 那这也好写了 状态有i，j二维，可以看成一个表，终点是i-1， j-1
# 初始已知的边界是i == -1 和 j == -1时（想象左边和上边加了一行和一列，表示-1时）
# 那么怎么遍历都行，只要算的时候之前的状态已经算过就行
# 这里一行一行来。

# 方法三
        # 先构建初始数组，并初始化边界
        # 一定要明白，这里多加的一行和一列是最左边和最上边加的，
        # 对应暴力递归方法里的当i == -1 和j == -1时的情况
        # 相应的，dp里的索引i，j，对应着word1[i-1] 和word2[j-1]
        m = len(word1) + 1
        n = len(word2) + 1

        # dp = [[0] * n] * m  不能这么构建二维数组，这样是共享内存的……
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 0
        for i in range(1, n):
            dp[0][i] = i
        for i in range(1, m):
            dp[i][0] = i
        

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m-1][n-1]