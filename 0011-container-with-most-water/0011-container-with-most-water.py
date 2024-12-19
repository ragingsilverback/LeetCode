class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while(left<right):
            volume = (right-left)*min(height[left],height[right])
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
            ans = max(ans,volume)

        return ans



        