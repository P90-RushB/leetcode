class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # dfs或者bfs都可以

        # 方法1， dfs 迭代 栈
        if newColor == image[sr][sc]: return image
        stack = [(sr, sc)]
        old = image[sr][sc]
        
        while stack:
            a, b = stack.pop()
            image[a][b] = newColor
            for p, q in zip((a, a, a+1, a-1), (b+1, b-1, b, b)): 
                if 0 <= p < len(image) and 0 <= q < len(image[0]) and image[p][q] == old:
                    stack.append((new_i, new_j))
        return image

        # 方法2 dfs 递归
        if image[sr][sc] != newColor:
            old, image[sr][sc] = image[sr][sc], newColor
            for i, j in zip((sr, sr+1, sr, sr-1), (sc+1, sc, sc-1, sc)):
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == old:
                    self.floodFill(image, i, j, newColor)
        return image。

        # 方法3 bfs
        from collections import deque
        q = deque()
        if not image or not image[0]:
            return image
        if image[sr][sc] == newColor:
            return image
        m = len(image)
        n = len(image[0])

        org = image[sr][sc]
        q.append((sr, sc))
        while q:
            a, b = q.popleft()
            image[a][b] = newColor
            for i, j in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                if 0 <= i < m and 0<= j < n:
                    if image[i][j] == org:
                        q.append((i, j))
        return image
