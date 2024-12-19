class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        temp = []
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i]==key:
                temp.append(i)

        if len(temp)==0:
            return temp

        for i in range(n):
            for j in temp:
                if abs(j-i)<=k:
                    ans.append(i)
                    break
        
        return ans



        