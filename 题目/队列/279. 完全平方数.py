class Solution:
    def numSquares(self, n: int) -> int:
        # 这是是我自己的写法，bst的。

        ################官方题解中有其他解法。其中dp解法已经要看看。

        # 理解了bst后豁然开朗
        # 这题说最少，就和找路径里最短一样，那不就是bst。
        # 类似于层序遍历，第一次，把所有小于n的完全平方数加入，并且保存减去平方数之后的数。
        import math
        from collections import deque
        
        if int(math.sqrt(n))**2 == n:
            return 1
        
        cnt = 1
        
        
        # 存所有小于n的完全平方数
        tmp_list = [i for i in range(1, n) if int(math.sqrt(i))**2 == i]
        # num_idx = {v:k for k,v in enumerate(tmp_list)}
        
        
        queue = deque()
        for i in tmp_list:            
            queue.append((i, n-i))
        
        while queue:
            
            cnt += 1
            size = len(queue)
            
            for _ in range(size):
                now, rest = queue.popleft()
                for i in tmp_list:
                    if i > now:
                        break
                    if i == rest:
                        return cnt
                    if rest - i >0:
                        queue.append((i, rest-i))
                    
        return n

# 二刷
        # 求最少需要的完全平方数的个数。
        # 关键是怎么类比成路径的搜索，就好做了。
        # 一个很容易想到但是实际上错误的解法是：贪心：
            # 从最大的完全平方数开始，这其实有点贪心的思想了，如果一直向前算得到了解，那就结束了，就是最短，
        # 贪心实际上并不能保证数最少，可能伴随很多1的平方结尾。
        
        # 还是bfs
        # 如果小于某个数的完全平方数只有1（也就是小于4），那就需要那么多个1
        from collections import deque
        q = deque()
        all_nums = []
        for i in range(1, n):
            if i**2 > n:
                break
            if i ** 2 == n:
                return 1
            all_nums.append(i**2)
            q.append(n - i**2)
        
        cnt = 1

        while q:
            n = len(q)
            for _ in range(n):
                tmp = q.popleft()
                if tmp in all_nums:
                    return cnt + 1
                for i in all_nums:
                    if tmp > i:
                        q.append(tmp - i)
            cnt += 1
        return cnt