class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat = 0
        left = 0
        right = len(nums)-1
        while(left<=right):
            if(left!=right):
                concat += int(str(nums[left]) + str(nums[right]))
            else:
                concat += int(str(nums[left]))
            left +=1
            right -=1

        return concat
        