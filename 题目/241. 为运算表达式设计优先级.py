class Solution:
    # 分治，这是一道看的懂但难写的出来的题
    memo = {}
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        if input in self.memo:
            return self.memo[input]
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in range(len(left)):
                    for k in range(len(right)):
                        if input[i] == '+':
                            res.append(left[j] + right[k])
                        elif input[i] == '-':
                            res.append(left[j] - right[k])
                        else:
                            res.append(left[j] * right[k])
        if len(res) == 0:
            res.append(int(input))
        self.memo[input] = res
        return res