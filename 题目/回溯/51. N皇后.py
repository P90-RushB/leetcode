class Solution:
    # 卧槽我竟然直接写对了。同样是回溯算法，N皇后问题和全排列可以说其实一毛一样。
    # 只要labuladong的全排列看懂了，回溯算法都是那个模板套路，也就是n叉树的遍历，在
    # 先序的时间点做选择，在后序的时间点做撤销选择。

    def solveNQueens(self, n):
        # 回溯算法
        from copy import copy
        res = []
        track = []

        def helper():
            # 做选择
            for i in range(n):

                # 递归的终止条件：当已经查找到棋盘最后一行，就得到一种解法，存入res
                if len(track) == n:
                    res.append(copy(track))
                    return 
                    
                # 这块代码用来判断第 len(track)行， 第i列 那个格子 是否可以放置皇后，如果不能，就continue
                # 类似于全排列时，做选择要剔除已经选取过的路径，这里要剔除的是
                # 非法的格子。非法的格子是根据题目要求的，在选择第i行的格子时，
                # 前i-1行所选的已经存在track数组中，第i行所选的格子不能与前面的
                # 每个选择的格子在同一列，也不能位于斜45度的方向（也就是不能位于左下
                # 或者右下）
                if track:
                    fuhe = True
                    for k,v in enumerate(track):
                        # 如果位于前面某个已选格子的斜下方 or 在同一列
                        if abs(k- len(track)) == abs(v - i) or i==v:
                            fuhe = False
                            break
                    if not fuhe:
                        continue

                track.append(i)

                helper()

                track.pop()

        helper()

        # res的每个索引代表每一行，值代表每行应该放在第几格
        # 下面只是将res解析成题目要求的  ..Q..的形式。
        for i in range(len(res)):
            tmp = res[i]
            new = []
            for j in tmp:
                new.append('.' * j + 'Q' + '.' * (n-1-j))
            res[i] = new

        return res
    
s = Solution()
res = s.solveNQueens(4)

print(res)