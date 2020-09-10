class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        direction = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1],
        [-1, 0], [-1, 1]]
        m = len(grid)
        n = len(grid[0])
        queue = []
        queue.append((0,0))
        pathLength = 0
        while len(queue) != 0:
            size = len(queue)
            pathLength += 1
            while size > 0:
                size -= 1
                cur = queue.pop(0)
                cr = cur[0]
                cc = cur[1]
                if grid[cr][cc] == 1:
                    continue
                if (cr == m -1 and cc == n - 1):
                    return pathLength
                grid[cr][cc] = 1
                for d in direction:
                    nr = cr + d[0]
                    nc = cc + d[1]
                    if nr < 0 or nr >= m or nc < 0 or nc >=n:
                        continue
                    queue.append((nr, nc))
        return -1