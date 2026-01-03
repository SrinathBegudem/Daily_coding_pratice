class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        The intution here is ato form a graph with forawrd and backward dir 
        having different weight
        - Given an edge list eqs 
        - from rules of graphs data stucture we know that we can traverse edge list directly, so we need to convert the edge list into adj list ( dict or list). i would like to go with dict here for similicity.
        - while building and adj list i will add its wieghts too both in forward dir which is the values and reverse dir which is the inverse of the values 
        """
        #step1: create the adj list grpah 
        graph = dict()
        # i will use enumerate so that the index can be used for fetch values
        for i, eq in enumerate(equations):
            val = values[i]
            a,b = eq
            #forward edge a - > b
            if a not in graph: 
                # if a is not in graph first create it and then append the val
                graph[a] = []
            graph[a].append([b,val])
            #backwards edge b - > a
            if b not in graph:
                #if b is not in graph add it 
                graph[b] = []
            graph[b].append([a,1/val]) # inverse of the val
            
        # # the above can be simplified by deafaultdict
        # graph = deafaultdict(list) # creates vals of list default
        # for i, eq in enumerate(equations):
        #     val = values[i]
        #     a,b = eq

        #     graph[a].append([b,val])
        #     graph[b].append([a,1/val])

        #step2: is to do bfs/dfs on each query to find the path from a - > b 

        def bfs(start,end):
            # edge case there might be a chnace that one of the start or end location is not in eq or not possible to eq 
            if start not in graph or end not in graph:
                return -1 
            
            q = deque([(start,1)]) # we start with 1 because 1 is neutral and we acc res
            visited = set()
            visited.add(start)

            while q:
                node,wei = q.popleft()
                # if we found out the end we simply return 
                if node == end:
                    return wei
                
                for nei,cur_wei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,wei*cur_wei)) # add the accumalted result to the queue

            return -1 # edge case if both the nodes are in the grpah but there is not path connecting them so we return -1 
        
        # return [bfs(a,b) for a,b in queries]

        def dfs(start,end,visited):
            #base condition 
            if start == end: return 1.0 

            visited.add(start)

            for nei, wei in graph[start]:
                if nei not in visited:
                    res = dfs(nei,end,visited)
                    if res != -1:
                        return res * wei
            return -1 # very imp edge case if forget will give error as the dfs return None type
        res = []
        for a,b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a,b,set()))
        
        return res
            











        # DFS function to find product from start to end
        def dfs(start, end, visited):
            if start == end:
                return 1.0

            visited.add(start)

            for nei, weight in graph[start]:
                if nei in visited:
                    continue
                result = dfs(nei, end, visited)
                if result != -1:  # found a valid path
                    return result * weight

            return -1
