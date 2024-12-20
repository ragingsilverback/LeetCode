class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        if n==1:
            return abs(k-nums[0])
        median = n//2
        if nums[median]==k:
            return 0
        
        for i in range(0,median):
            if nums[i] > k:
                count += nums[i]-k
        for i in range(median+1,n):
            if nums[i] < k:
                count += k-nums[i]
        count += abs(nums[median]-k)

        return count



        