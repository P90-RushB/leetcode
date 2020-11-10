class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # 如果从第一行开始迭代，每行是指数级增长，肯定爆掉。
        # 真正做法：
        # 第n行的每个数，对应前一行的某个数。
        # 第n行的第k个数，对应第n-1行的 k/2 个数，且如果k%2 = 0，则两者相等，
        # 如果余数等于1，则两者相反(0变1,1变0)

        # 题目是从第一行第一个数开始，这里用helper封装一下，映射到从第0行第0个数开始，方便计算。
        def helper(N, K):
            # 边界
            if N == 0:
                return 0

            # 递归
            pre= helper(N-1, K // 2)
            first = K % 2 == 0
            return pre if first else (-1*pre + 1)

        return helper(N-1, K-1)
 


