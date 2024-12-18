class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        even = 0
        n = len(nums)

        while even<n and odd<n:
            if nums[even]%2==0:
                even += 2
            if nums[odd]%2==1:
                odd += 2
            else:
                nums[even],nums[odd] = nums[odd],nums[even]

        return nums

            


        
            
        
        