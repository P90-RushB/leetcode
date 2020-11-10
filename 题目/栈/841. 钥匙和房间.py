class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # 方法1 dfs 递归 递归方式是看的官方题解。
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n

        # 方法2， dfs 迭代
        # n = len(rooms)
        # visited = set()
        # visited.add(0)
        # stack = rooms[0]
        # while stack:
        #     tmp = stack.pop()

        #     if tmp in visited:
        #         continue
        #     visited.add(tmp)

        #     stack += rooms[tmp]
        # return len(visited) == len(rooms)

        # 方法3 bfs
        # n = len(rooms)
        # visited = set()
        # from collections import deque
        # q = deque()
        # q.append(0)
        # visited.add(0)

        # while q:
        #     tmp = q.popleft()

        #     next_door = rooms[tmp]
        #     for i in next_door:
        #         if i in visited:
        #             continue
        #         visited.add(i)
        #         q.append(i)

        # return len(visited) == len(rooms)