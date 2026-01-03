class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        key idea here is 
        - we cannot do dfs and bfs with edge list, it is very inefficent, we need to scan entire edge list every time which is terrible time complexity 
        - Convert into adj list or adj dict
        - Pattern : after converting its bfs/dfs for disconnected graphs 
        """
        # converting edge list to adj dict
        #create a graph node with empty lists
        graph = {i:[] for i in range(n)}

        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
        num_comp = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                num_comp += 1
                visited.add(node)
                bfs(node)
        return num_comp





#------------ second try---------
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #lets quickly build the adj list(dict)
        graph = dict()
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append(b)
            graph[b].append(a)
        
        # visited = set()
        # def dfs(node):
        #     visited.add(node)

        #     for nei in graph.get(node,[]):
        #         if nei not in visited:
        #             dfs(nei)
        
        # components = 0
        # for node in range(n):
        #     if node not in visited:
        #         components += 1
        #         dfs(node)
        # return components







        visited = set()
        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                node = q.popleft()

                for nei in graph.get(node,[]):
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                bfs(node)
        return components        
                
                

        