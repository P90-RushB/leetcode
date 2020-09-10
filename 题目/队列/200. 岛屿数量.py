class Solution:
    # 这题可以bfs，也可以dfs，dfs又可以递归或者显式栈，下面用递归来解决。
    def numIslands(self, grid: List[List[str]]) -> int:
        # 用dfs递归来解决。
        # 遍历节点，对每个节点，如果是1，则res+1，并调用一次递归清0，调用一次
        # 会递归清0所有相邻的1.
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs_clear1(i,j):

############### 可替换的递归和显式栈两种方法 ####################
            # 方式1，显式栈 与方法二注释一个，都能运行。
            s = [(i,j)]
            while s:
                p,q = s.pop()
                grid[p][q] = '0'
                for a,b in [(p,q+1), (p, q-1), (p-1,q), (p+1,q)]:
                    if 0<=a<m and 0<=b<n:
                        if grid[a][b] == '1':
                            s.append((a,b))

            # 方法二，递归
            # grid[i][j] = '0'
            # for a,b in [(i,j+1), (i, j-1), (i-1,j), (i+1,j)]:
            #     if 0<=a<m and 0<=b<n:
            #         if grid[a][b] == '1':
            #             dfs_clear1(a,b)
########################################################

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_clear1(i,j)
        return res

############################ bfs ############################
        # 用bfs解决
        # 遍历节点，对每个节点，如果是1，res+1，并开始一次bfs，
        # 即用一个队列，从该节点开始，把所有相邻的1都广度优先，置0.
        from collections import deque
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    # 开始bfs
                    q = deque()
                    q.append((i,j))

                    # 可选一 grid[i][j] = '0'可以写在这里,  也就是bfs之前，先把该位置置0
                    # grid[i][j] = '0'

                    while q:
                        a,b = q.popleft()

                        # 可选二，grid[a][b] = '0'也可以写在这里。在bfs过程中，除了第一个元素在这里置0，
                        # 其他元素在下方append到queue之前，已经置0了。 
                        grid[a][b] = '0'

                        for u,v in [(a,b+1), (a, b-1), (a-1,b), (a+1,b)]:
                            if 0<=u<m and 0<=v<n:
                                if grid[u][v] == '1':
                                    # 一定要在这里进行置0操作，而不能依赖于可选二处的置0，否则会超时。因为
                                    # 如果在可选二处也就是才置0，这个元素可能会被周围好几个元素影响入队，入队
                                    # 好几次，重复。
                                    grid[u][v] = '0'
                                    q.append((u,v))
        return res