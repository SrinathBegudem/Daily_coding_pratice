from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        This is a classic bfs and dfs problem graph
        """

        def dfs():
            #uses stacks 
            stack = [0] # room no 0 is always unlocked 
            visited = set()# to see what all rooms we visited 
            visited.add(0)
            while stack:
                room = stack.pop()

                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
                        visited.add(key)
            return len(visited) == len(rooms)
        # return dfs()


        def bfs():
            #uses queue
            q = deque([0])
            visited = set()
            visited.add(0)

            while q:
                room = q.popleft()
                
                for key in rooms[room]:
                    if key not in visited:
                        q.append(key)
                        visited.add(key)
            return len(visited) == len(rooms)
        return bfs()





        
    