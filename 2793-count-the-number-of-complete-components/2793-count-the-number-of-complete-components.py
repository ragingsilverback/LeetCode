class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components= []

        def create_adjlist(n,edges):
            adjlist = {i : [] for i in range(n)}
            for u,v in edges:
                adjlist[u].append(v)
                adjlist[v].append(u)
            return adjlist

        adjlist = create_adjlist(n,edges)

        def dfs(start,adjlist,visited,component):
            visited.add(start)
            component.append(start)
            for neighbour in adjlist[start]:
                if neighbour not in visited:
                    dfs(neighbour,adjlist,visited,component)

        for i in range(n):
            if i not in visited:
                component = []
                dfs(i,adjlist,visited,component)
                components.append(component)

        count = 0
        for component in components:
            nodes = len(component)
            links = 0
            for node in component:
                links = links + len(adjlist[node])
            if links//2==nodes*(nodes-1)//2:
                count +=1

        return count



        