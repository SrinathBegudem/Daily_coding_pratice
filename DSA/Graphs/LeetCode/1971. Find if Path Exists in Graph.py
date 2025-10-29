from collections import deque
class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        The idea here is to 
        - convert the edge list to adjacency list because we cannot direclty apply bfs or dfs with out it.
        - then traverse the graphs either with bfs or dfs 
        Time and space 
        - time = (V + E) Traversing each vertex and its edges
        - space = (V+E) storing vertix and its edges in 2d list

        """
        #edge case if source == destination return True
        if source == destination:
            return True


        def convert_to_ada_list(edge_list,n):
            """
            Given edge list we convert it into adjacency list
            key points:
            - while ada_list dont do adj = [list()] * n or adj = [[]] * n, because This creates n references to the same list in memory.So if you modify one, all others change too
            - 
            """
            ada_list = [list() for _ in range(n)]  # or [[] for _ in range(n)]
            for s,d in edge_list:
                ada_list[s].append(d) # since its bi direction s to d 
                ada_list[d].append(s) # and d to s 
            return ada_list

        def bfs(graph,start,destination):
            """
            the intuition here is to have classic bfs traversal for graphs 
            - we will have a queue for level order traversal 
            - and check if we can reach from source to destionation
            - if yes we will print True
            """
            q = deque([start]) # queue to micmic level order traversal
            visited = set() # to track the already visited nodes
            visited.add(start)
            res = []
            while q:
                node = q.popleft()
                res.append(node)

                for neighbours in graph[node]: # get the all nieghbors of particular node
                    print(neighbours,destination)
                    # we can add one more cond to check if we are at destination
                    if neighbours == destination:
                        return True # return as its reachable

                    if neighbours not in visited: # if nieghbour is not visited
                        visited.add(neighbours) # mark as visited
                        q.append(neighbours)
            return False

        graph = convert_to_ada_list(edges,n)
        return bfs(graph,source,destination) # not reachable 
        