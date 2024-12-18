class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        dic = {}

        while i<len(nums1) and j<len(nums2):
            if nums1[i][0]==nums2[j][0]:
                s = nums1[i][1] + nums2[j][1]
                dic[nums1[i][0]] = dic.get(nums1[i][0],0) + s
                i +=1
                j +=1
            else:
                if nums1[i][0] < nums2[j][0]:
                    dic[nums1[i][0]] = dic.get(nums1[i][0],0) + nums1[i][1]
                    i += 1
                else:
                    dic[nums2[j][0]] = dic.get(nums2[j][0],0) + nums2[j][1]
                    j += 1

        while i<len(nums1):
            dic[nums1[i][0]] = dic.get(nums1[i][0],0) + nums1[i][1]
            i += 1
        while j<len(nums2):
            dic[nums2[j][0]] = dic.get(nums2[j][0],0) + nums2[j][1]
            j += 1

        dic = sorted(dic.items())
        sol = list(dic)
        return sol


        
         
        
        