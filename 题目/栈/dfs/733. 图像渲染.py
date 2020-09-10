class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # dfs或者bfs都可以
        # 这里不用加visited这个备忘录是因为可以if判断是否某个位置等于原始颜色值。如果不等，是不会进去的，
        # 而如果等于，就会重置颜色，下次就不等了，等于天然有个备忘录。
        if not image or not image[0]:
            return image
        
        m = len(image)
        n = len(image[0])

        # visited = set()

        origin_color = image[sr][sc]
        if origin_color == newColor:
            return image

        def set_color(r, c):
            # if image[r][c] == origin_color:
                # visited.add((r, c))
            image[r][c] = newColor
            for a,b in [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]:
                if 0 <= a < m and 0 <= b < n and image[a][b] == origin_color:
                    set_color(a, b)

        set_color(sr, sc)
        return image
        

        