class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        k = 0
        for i in range(len(nums)):
            if nums[i]<pivot:
                smaller.append(nums[i])
            if nums[i]>pivot:
                greater.append(nums[i])
            if nums[i]==pivot:
                k +=1

        sol = []
        for num in smaller:
            sol.append(num)
        for i in range(k):
            sol.append(pivot)
        for num in greater:
            sol.append(num)

        return sol



        