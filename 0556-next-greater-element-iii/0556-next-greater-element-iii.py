class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        
        l = len(nums)
        i = l-2
        while i>=0 and nums[i]>=nums[i+1]:
            i -=1

        if(i<0):
            return -1
        
        j = l-1
        while(nums[j]<=nums[i]):
            j -=1
        nums[j],nums[i] = nums[i],nums[j]

        nums[i+1:] = reversed(nums[i+1:])

        result = int("".join(map(str,nums)))
        return result if result <= 2**31-1 else -1



            
