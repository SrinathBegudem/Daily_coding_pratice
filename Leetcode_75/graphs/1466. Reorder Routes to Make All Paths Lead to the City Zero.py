from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        This problem is really mess, i spent around 4 hr to udnertsadn chatgpt given code.
        but the code from depthi talseri youtubue is easy intutively 

        Key points:
        - This chatgpt sol only works when they give that is graph works as tree>
        - In the grpah when there are no cycles and we can only traverse from parent(node) to child node but not back this is tree, this probelem is tree like problem.

        """

        def simple_sol():
            """
            The intuition here is 
            - Rule: we cannot traverse edge list, so when ever edge list given convert it into adjlist (graph or list). 
            Idea:
            - so we are given a directed graph to find the reversed nodes, we create undirected adj graph
            - we also parellely add the edge list elements to set for o(1) lookups 
            - the idea here is we do level order traverse, why?
            - so lets start with ex1: from node 0,
            - take the neigh of node 1, which is 1,4
            - 1 is not pointing towards the 0 (bad direction) so we need to reverse it, increase reverse counter += 1
            - now 4 is pointing towards 0 good(direction)
            - now we take neigh of 1 and 4 if they are pointing towards 1 and 4 then they are in good direction( which means they are indirectly pointing towards 0) as we changed the direct( not in the problem but we assume) of 1 which is now pointing towards 0, similarly 4 is laready pointing towards 0. so , node pointing towards 4 will indirectyl point towards the node 0.
            Thats the intution.
            - we do level order traversly and check if they are pointing towards there parent node is yes they are good nodes if not they are bad nodes we need to revrese it.
            """
            # main intuition “Is neighbor pointing to parent? If not, reverse it.”

            #step 1: edge list to adj list and parelley also add the edge list ele to set
            graph = {key:[] for key in range(n)}
            edges = set()
            for start,end in connections:
                #add the orginal direction
                graph[start].append(end)
                #add its reverse direction
                graph[end].append(start)
                #now add elements to edges set 
                edges.add((start,end))
            
            #step2: we can do bfs level order traversal either with deque or naturally with lists:
            #solution with lists and naturally level order traversal
            cur_level = [0]
            visited = set()
            visited.add(0)
            changes = 0
            while cur_level:
                #which stored the nodes of new level
                new_level = []
                #we traverse cities in cur_lev
                for city in cur_level:
                    #then for each city we traverse it neig
                    for nei in graph[city]:
                        #if its not in visited, we visit it and append it to new level
                        if nei not in visited:
                            visited.add(nei)
                            new_level.append(nei)
                            # if dont have good direction edge nei - > city then add changes
                            if (nei,city) not in edges:
                                changes += 1
                #update the cur_level = new_level
                cur_level = new_level

            return changes
        return simple_sol()

            # #solution with deque
            # q = deque([0])
            # visited = set()
            # visited.add(0)
            # changes = 0
            # while q:
            #     level_size = len(q)

            #     for _ in range(level_size):
            #         city = q.popleft() # we need to point the neig to this city 

            #         for nei in graph[city]:
            #             if nei not in visited:
            #                 q.append(nei)
            #                 visited.add(nei)
            #                 # if there is no edge from nei to city in edges that means its in wrong direction, we are doing level by level checking whether its nei is pointing towards the parent (i.e city)
            #                 if (nei,city) not in edges: # if there is no nei -> city then we will have to reverse it.
            #                     changes += 1
            # return changes
        
        # return simple_sol()



                
        def chatgpt_code():
            """
            
            """
            graph = {i: [] for i in range(n)}

            # Build adjacency list
            for u, v in connections:
                graph[u].append((v, 1))  # original direction u -> v
                graph[v].append((u, 0))  # reverse direction v -> u
            
            visited = set()

            def dfs(node):
                visited.add(node)
                changes = 0

                for nei, direction in graph[node]:
                    if nei not in visited:
                        changes += direction      # add 1 if edge is BAD
                        changes += dfs(nei)       # add changes from deeper levels
                
                return changes

            return dfs(0)