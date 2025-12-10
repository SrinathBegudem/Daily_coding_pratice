class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The key idea here is
        - have 2 pointer one at start and another at end 
        - area = l * b , where l is the distance btw 2 pointers and b is min height of both i,j pointers
        - cal the max_are and update as we proceed
        """
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            l = end - start
            b = min(height[start],height[end])
            area = l * b
            # if area > max_area: # instead of this use python max which is cleanrer and faster
            #     max_area = area
            # update the pointers based on the hieght, # move the shorter line
            max_area = max(area,max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area

        