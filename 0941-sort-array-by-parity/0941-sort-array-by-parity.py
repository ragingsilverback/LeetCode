class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i],nums[odd] = nums[odd],nums[i]
                odd += 1

        return nums
        