class Solution:
    def numDecodings(self, s: str) -> int:
        # https://cloud.tencent.com/developer/article/1407015
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0": 
            return 0
        if len(s) == 1:
            return 1
        dp = [1,1]
        for i in range(2, len(s)+1):
            # print dp, s[i-2:i]
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0': # 当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])  # 当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]
            elif s[i-1]!='0':  # 
                dp.append(dp[i-1])  # 当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]
            else:
                return 0
        return dp[-1]