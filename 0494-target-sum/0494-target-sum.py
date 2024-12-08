class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        aim = target+sum(nums)
        if(aim%2!=0 or aim<0):
            return 0
        
        
        aim = aim//2
        n = len(nums)

        dp = [[0]*(aim+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(0,aim+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

        return dp[-1][-1]

        

        
        