class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def create_adj_list(n,edges):
            adj_list = {i:[] for i in range(n)}
            for u,v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list

        def dfs(start,n,visited,adj_list):
            visited.add(start)
            for neighbour in adj_list[start]:
                if neighbour not in visited:
                    dfs(neighbour,n,visited,adj_list)

        visited = set()
        adj_list = create_adj_list(n,edges)

        dfs(source,n,visited,adj_list)

        return destination in visited
            
        