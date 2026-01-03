class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # let me convert the board into 1d str
        #index    0 1 2 3 4 5
        target = "123450"
        
        #covnert the start into string
        start =  "".join(str(board[r][c]) for r in range(len(board)) for c in range(len(board[0])))

        # this are all the index that one number can move from 0,1,2,3,4,5 indexs based on board
        swaps = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [3,1,5],
            [4,2]
        ]


        # let me find the index where the 0 is located for given start posiiton
        index = -1 
        for i in range(len(start)):
            if int(start[i]) == 0:
                index = i
        
        #Neetcode did .index method but we did manual index finding by our own which is fine and great.
        q = deque([(start,index,0)]) # start, position, index , moves

        visited = set()
        visited.add(start)

        while q:
            state,index,moves = q.popleft()

            if state == target : return moves

            # for each possible swaps we # swap with 0
            for pos in swaps[index]:
                new_state = list(state) # its easy to work with list just note the elements inside the list are still str objects
                
                # swap with 0
                new_state[pos],new_state[index] = new_state[index],new_state[pos]
                s_new_state = "".join(new_state)

                if s_new_state not in visited:
                    q.append((s_new_state,pos,moves+1))
                    visited.add(s_new_state)
        return -1 