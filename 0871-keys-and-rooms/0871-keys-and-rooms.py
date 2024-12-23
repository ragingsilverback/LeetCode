class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(start,visited):
            visited.add(start)
            for keys in rooms[start]:
                if keys not in visited:
                    dfs(keys,visited)

        dfs(0,visited)

        return len(rooms)==len(visited)


        
        