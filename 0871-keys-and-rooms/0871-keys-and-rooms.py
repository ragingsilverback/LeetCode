class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def create_adjlist(rooms):
            adjlist = {i:[] for i in range(len(rooms))}
            for i in range(len(rooms)):
                adjlist[i] = [key for key in rooms[i]]
            return adjlist

        visited = set()
        adjlist = create_adjlist(rooms)

        def dfs(start,visited,adjlist):
            visited.add(start)
            for neighbour in adjlist[start]:
                if neighbour not in visited:
                    dfs(neighbour,visited,adjlist)

        dfs(0,visited,adjlist)

        return len(rooms)==len(visited)


        
        