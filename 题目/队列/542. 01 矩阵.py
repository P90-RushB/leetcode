class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 这是我写的bfs，完美。 官方题解里的dp方法记得看一下，我没想出来dp怎么做。
        # bfs，等于0的地方，值为0， 记录visited过。
        # 每次对每个0相邻的四个方向延申，如果没有visited过，就标记，并且赋值。
        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        from collections import deque
        q = deque()
        
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                    
        res = 0
        while q:
            
            res += 1
            cnt = len(q)
            
            for _ in range(cnt):
                a,b = q.popleft()

                for i, j in [(a,b+1), (a,b-1), (a-1,b), (a+1, b)]:
                    if 0<=i<m and 0<=j<n:
                        if (i,j) not in visited:
                            visited.add((i,j))
                            q.append((i,j))
                            matrix[i][j] = res  
        return matrix