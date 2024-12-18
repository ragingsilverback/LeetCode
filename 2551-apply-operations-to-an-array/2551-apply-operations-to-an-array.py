class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
                i += 2
            else:
                i +=1
        zero = 0
        for i in range(0,n):
            if nums[i]!=0:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero +=1
        
        return nums
        
        