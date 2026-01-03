class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Question 1: No Cycle = Topological Sort Always Possible?
        YES! This is ALWAYS true.
        """

        # do dfs cycle detection if not cycle that means we can complete all the course 

        #build the adj grpah first
        graph = dict()
        # for a,b in prerequisites:
        #     if a not in graph:  no dont do this 
        #         graph[a] = []
        #     graph[a].append(b) # a -> b
        for a,b in prerequisites:
            if b not in graph:  
                graph[b] = []
            graph[b].append(a) # a -> b

        # we will do topological sort for this 
        visited = set()
        path = set()
        def dfs(node):

            if node in path:
                return True # cycle found

            if node in visited:
                return False # this node completely visited
            
            # add the cur node to the path 
            path.add(node)
            #traverse the depths of cur node ( recursion)
            for nei in graph.get(node,[]):
                if dfs(nei):
                    return True

            path.remove(node)
            visited.add(node)
            return False

        # for node in range(numCourses):
        #     if node not in visited:
        #         if dfs(node):
        #             return False
        # return True


        def bfs():
            """
            That makes the edge mean: a must be taken before b (the opposite of the problem statement).
            What’s wrong with your current code’s interpretation

You did:

graph[a].append(b)   # a -> b
in_deg[b] += 1


That makes the edge mean: a must be taken before b (the opposite of the problem statement).

So your in_deg is no longer “prerequisites needed for this course”.
It becomes something like: “how many courses depend on this course (in the original meaning)”, because you flipped the relationship.

Important point

For 207 (just True/False), flipping all edges still keeps cycles as cycles, so you can still detect a cycle and often still pass.

But:

your queue will start with “courses nobody depends on” (sinks),

the produced order (if you returned it) would not represent a valid “take prereqs first” plan,

it becomes confusing fast, and it will hurt you on Course Schedule II (210).
        universal remeber 
        graph[prerequisite].append(course)
        in_degree[course] += 1
        
        or more genrally 
    
        graph[comes_first].append(comes_after)
        in_degree[comes_after] += 1
            """
            graph = dict()
            in_deg = [0] * numCourses

            for a,b in prerequisites:
                if b not in graph:
                    graph[b] = []
                # graph[a].append(b) # a > b # wrong
                # in_deg[b] += 1
                graph[b].append(a) # a > b # wrong look at pattern notes dont go on order go on wording
                in_deg[a] += 1               
            
            q = deque()
            # add course that dont have any dependcies at the top
            for course in range(len(in_deg)):
                if in_deg[course] == 0:
                    q.append(course)

            courses_taken = 0

            while q:
                node = q.popleft()
                courses_taken += 1
                for nei in graph.get(node,[]):
                    in_deg[nei] -= 1

                    if in_deg[nei] == 0:
                        q.append(nei)
            return courses_taken == numCourses
        return bfs()
        