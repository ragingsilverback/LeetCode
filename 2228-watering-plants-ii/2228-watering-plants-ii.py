class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        i,j = 0, n-1
        A = capacityA
        B = capacityB
        refill = 0
        while(i<=j):
            if(i==j):
                if(max(A,B)<plants[i]):
                    refill +=1
                break
            if plants[i]>A:
                refill += 1
                A = capacityA
            A = A - plants[i]

            if plants[j]>B:
                refill +=1
                B = capacityB
            B = B - plants[j]
   
            i +=1
            j -=1

        return refill
        