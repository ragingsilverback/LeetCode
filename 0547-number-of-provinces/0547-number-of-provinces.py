class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(start,isConnected,visited):
            visited.add(start)
            for i in range(len(isConnected)):
                if isConnected[start][i]==1 and i not in visited:
                    dfs(i,isConnected,visited)
        
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                count +=1
                dfs(i,isConnected,visited)

        return count

        