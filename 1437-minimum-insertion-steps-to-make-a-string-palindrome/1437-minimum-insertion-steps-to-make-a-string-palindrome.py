class Solution:
    def minInsertions(self, s: str) -> int:
        if(s==s[::-1]):
            return 0

        n = len(s)
        t = s[::-1]

        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        lps = dp[-1][-1]

        return (n-lps)


        