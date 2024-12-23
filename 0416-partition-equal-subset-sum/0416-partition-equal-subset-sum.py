class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if (target%2!=0):
            return False

        target = target//2
        n = len(nums)
        dp = [[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[-1][-1]
        

        
        