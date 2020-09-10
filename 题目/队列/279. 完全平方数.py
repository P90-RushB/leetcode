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