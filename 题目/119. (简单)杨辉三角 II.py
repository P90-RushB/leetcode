class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 简单，一行一行来。

        pre = [1]
        if rowIndex == 0:
            return pre
        cnt = 0
        for i in range(1, rowIndex+1):
            now = [1] * (len(pre) + 1)
            for j in range(1, len(now)-1):
                now[j] = pre[j-1] + pre[j]

            cnt += 1
            if cnt == rowIndex:
                return now

            pre = now
        return -1