class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        """
        For every ---- spot there are 10 options so all 4 have 10 ** 4 as they are all independent event so gets mutiplied 
        """
        #step 1 : create a function called turn, because for every spot you can either do + 1 or -1 from cur position
        # total 8 possible children for one set of numbers
        def children(state):
            output = []
            temp = list(state)
            for  i in range(len(temp)):
                digit = int(temp[i])

                # turn up
                turn_up = (digit + 1) % 10
                temp[i] = str(turn_up)
                output.append("".join(temp))

                #turn down
                turn_down = (digit + 10 - 1) % 10
                temp[i] = str(turn_down)
                output.append("".join(temp))

                #restore the string start posiiton
                temp[i] = str(digit)
            return output
        # we will have a visited set to not to visit already visited combinations and also add deadends to that visited set so we dont go there as th equestion says if gone there you will be locked forecer
        visited = set(deadends)

        # if the starting combo is the deadlock then return immediately
        if "0000" in visited: return -1 

        #starting position
        q = deque([("0000",0)]) #lock,turn
        visited.add("0000")

        while q:
            lock,turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    q.append((child,turns+1))
                    visited.add(child)
        return -1 

                
            

# this child + str approch is better 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        def children(state):
            """
            This takes the cur state and produces 8 diff combination based on the cur state
            """
            res = []
            cur_state = state
            for i in range(len(cur_state)):
                digit = int(cur_state[i])

                up = (digit + 1) % 10
                up_str = cur_state[:i] + str(up) + cur_state[i+1:]
                res.append(up_str)

                down = (digit - 1 + 10) % 10
                down_str = cur_state[:i] + str(down) + cur_state[i+1:]
                res.append(down_str)
            return res



        def bfs():
            start = "0000"
            q = deque([(start,0)])
            visited = set(deadends)
            #edge case 
            if "0000" in visited: return -1

            #add edge case before adding start to the visited
            visited.add(start)


            while q:
                comb,steps = q.popleft()
                if comb == target:
                    return steps
                # print(children(comb))
                for child in children(comb):
                    if child not in visited:
                        q.append((child,steps+1))
                        visited.add(child)
            return -1


        return bfs()
