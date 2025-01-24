class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]

        for num,freq in freq_map.items():
            buckets[freq].append(num)

        sol = []
        count = 0
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                sol.append(num)
                count += 1
                if(count==k):
                    return sol
                
        