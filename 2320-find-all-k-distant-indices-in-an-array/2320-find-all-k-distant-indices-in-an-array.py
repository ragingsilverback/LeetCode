class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        temp = []
        sol = set()
        n = len(nums)
        for i in range(n):
            if nums[i]==key:
                temp.append(i)

        if len(temp)==0:
            return temp
        print(temp)

        for j in temp:
            for i in range(k+1):
                if(j-i>=0):
                    sol.add(j-i)
                if(j+i<=n-1):
                    sol.add(j+i)

        ans = sorted(list(sol))
        return ans



        