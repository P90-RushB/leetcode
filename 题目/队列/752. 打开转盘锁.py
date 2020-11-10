from collections import deque
class Solution:
    def openLock(self, deadends, target):

        # 我的写法和官方题解简直一毛一样，我也是666.
        # 可以看看官方题解对时间空间复杂度的分析。没看明白……
        
        # 一看最短路径，应该就是bfs。
        # 要有抽象出问题本质的思想。如果锁只有两位，从其实状态到target状态，
        # 会不会做？ 那不就等于一个二维地图，给了起始点坐标和目标点，中间的deadends就是不能走的
        # 障碍而已嘛？ 这只不过相当于状态是四维，没区别。
        
        # 按题意起始点可能是deadline，先判断下。
        if ['0000'] in deadends:
            return -1
        
        cnt = 0
        q = deque(['0000'])
        visited = set(['0000'])
        while q:
            tmp = q.popleft()
            if tmp == target:
                return cnt
            
            cnt+=1
            
            for i in range(4):
                string = ''.join([tmp[:i], str((int(tmp[i])+1)%10), tmp[i+1:]])
                if string not in deadends:
                    if string not in visited:
                        visited.add(string)
                        q.append(string)
                # 减1 就等于+9再取余
                string = ''.join([tmp[:i], str((int(tmp[i])+9)%10), tmp[i+1:]])
                if string not in deadends:
                    if string not in visited:
                        visited.add(string)
                        q.append(string)
        return -1

s = Solution()
count = s.openLock(["0201","0101","0102","1212","2002"], '0202')
print(count)

# 二刷，还是bfs就行。
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 求最小旋转次数，就是bfs
        if '0000' in deadends:
            return -1
            
        visited = set()
        from collections import deque
        q = deque()

        for i in deadends:
            visited.add(i)

        q.append('0000')
        cnt = 0
        while q:
            n = len(q)
            for _ in range(n):
                tmp = q.popleft()
                if tmp == target:
                    return cnt
                for i in range(4):
                    new_str1 = tmp[:i] + str((int(tmp[i])-1)%10) + tmp[i+1:]
                    new_str2 = tmp[:i] + str((int(tmp[i])+1)%10) + tmp[i+1:]

                    for k in [new_str1, new_str2]:
                        if k not in visited:
                            q.append(k)
                            visited.add(k)
            cnt += 1
        return -1