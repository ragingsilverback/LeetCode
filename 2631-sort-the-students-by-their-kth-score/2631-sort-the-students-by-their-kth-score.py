class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)-1):
            for j in range(i+1,len(score)):
                if score[j][k] > score[i][k]:
                    score[i],score[j] = score[j],score[i]

        return score

        