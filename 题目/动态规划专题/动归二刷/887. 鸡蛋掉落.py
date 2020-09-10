class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

################# 第二个加了二分的，虽然思路理解，我估计写不对，有空再看。
################# 这题的关键还是第一个基础版本：如何递归加备忘录
################# 所以实际上，并不算动归，因为不是自下而上算的（因为自下而上的下，分布太乱，不好写）

        # 递归加备忘录 然而还是超时了，需要再加上二分
        # memo = {}
        # def dp(K, N):
        #     if K == 1:
        #         return N
        #     if N== 0:
        #         return 0
        #     if (K, N) in memo:
        #         return memo[(K, N)]
            
        #     res = float('inf')
        #     for i in range(1, N+1):
        #         res = min(res,
        #         max(
        #             dp(K, N - i),
        #             dp(K - 1, i-1)
        #         ) + 1
        #         )
        #     memo[(K, N)] = res
        #     return res
        # return dp(K, N)

        # 递归加备忘录加二分
        memo = {}
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('inf')
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
                
            memo[(K, N)] = res
            return res
            
        return dp(K, N)

            