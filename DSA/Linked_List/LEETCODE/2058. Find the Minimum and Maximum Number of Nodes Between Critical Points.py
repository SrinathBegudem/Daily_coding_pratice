# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def optimal_sol():
            """
            The intuition here is 
            - i will have a intial crtical point and store its indx 
            - and for will hae prev critical point and use indx to cal the minima 
            - once we reach the end critical point 
            - we do intial cp - prevcp for maxima and as we traverse we find the minina 
            Time and space
            - Time = o(n)
            - space = o(1)
            """
            #base condition: we need atleast 3 points to have 1 critical point
            if not head or not head.next or not head.next.next:
                return [-1, -1]

            prev = head 
            cur = head.next 
            first_cp = -1
            prev_cp = -1
            min_dist = float('inf')
            indx = 1

            while cur.next:
                nxt = cur.next

                if (prev.val < cur.val > nxt.val) or (prev.val > cur.val < nxt.val):
                    if first_cp == -1:
                        first_cp = indx
                    else:
                        min_dist = min(min_dist, indx-prev_cp)
                    prev_cp = indx
                prev = cur
                cur = cur.next 
                indx += 1
            if prev_cp == first_cp:
                return [-1,-1]
            return [min_dist, prev_cp - first_cp]
        return optimal_sol()





        def brute_force():
            """
            The intuitio here is 
            - i collect all the crictical poitns 
            - for max distance i do diff of 0th and last index 
            - for min i do a loop to find the min distance and return them
            TIme and Space 
            - time = o(n)
            - space = o(k) # critical points we can optimsie this 
            """
            if not head or not head.next:
                return [-1, -1]
            prev = None
            cur = head
            
            # i stored all the critical poitns this can be optimsed to o(1)
            points = []
            count = 0 
            while cur and cur.next:
                prev = cur 
                cur = cur.next
                nxt = cur.next # this is cur.next.next (we already icreased the cur pointer above)
                count += 1
                if nxt and ((prev.val < cur.val > nxt.val) or (prev.val > cur.val and cur.val < nxt.val)):
                    points.append(count)
            print(points,count)
            if len(points) < 2: return [-1,-1]
            maxima = points[-1] - points[0]
            minima = float('inf')
            for i in range(1,len(points)):
                minima = min(minima,points[i] - points[i-1])
            return [minima,maxima]
                
        


        