class RecentCounter:

    def __init__(self):
        #we intilaise the counter 
        # store the incoming requests
        #sore the index becase if the request starting elements goes below the range given then we reduce the counter 
        #the condtion given is the incomign pigns will always be greater, so havng this idnex will help us to not to iterate again and again.
        self.counter = 0
        self.requests = []
        self.index = 0
    def ping(self, t: int) -> int:
        # lower_range = t - 3000
        # upper_range= t
        self.requests.append(t)
        # # if the incoming request is in range add coutner, this is always true if you see the. upper range its always t so just add it no need to check
        # if lower_range <= t <= upper_range:
        #     self.counter += 1
        
        self.counter+= 1
        
        # while the starting pings goes out of the range remove then from the counter, thsi code is optimsed
        while self.requests[self.index] < lower_range: #add self.index < len(self,request) at the begging of the wile loop becuase interviews liek defensive thinking while self.index < len(self,request) and  self.requests[self.index] < lower_range:
            self.counter -= 1
            self.index += 1
        return self.counter

# chatgpt praised my code i implemented queue with index and list but it gave me solution with deque
# chatgpt code
# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         # add current request
#         self.q.append(t)

#         # remove requests older than t - 3000
#         while self.q[0] < t - 3000:
#             self.q.popleft()

#         # remaining requests are within range
#         return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)