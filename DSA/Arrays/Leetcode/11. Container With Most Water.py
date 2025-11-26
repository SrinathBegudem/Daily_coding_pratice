class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Read the question carefully, all you need is to find the formual and the sum is done
        time = o(n)
        space = o(1)
        key point 
        - we move the shorter pointer (3) because area is. limited to the shorter pointer hieght and width
        - if we move the high hieght pointer from lets say 10 to 8 
        - the area is still width * 3, the hieght stays same because left is limiting the height
        """
        left = 0 
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                cur_area = height[left] * (right - left)
                left +=1
            else:
                cur_area = height[right] * (right - left)
                right -= 1
            max_area = max(max_area,cur_area)
        return max_area


        # the above code can be return in more concise way
        # max_area = 0
        # left = 0
        # right = len(height) - 1
        # while left < right:
        #     min_height = min(height[right],height[left])
        #     distance = right - left
        #     cur_area = min_height * distance
        #     if height[right] < hieght[left]:
            #    right -= 1
            # else:
            #    left += 1


    def maxArea(self, height: List[int]) -> int:
        """
        vol = l*b*h
        area = l*b
        we have to take min of both bars, so that water wont over flow and mutiply it with the distance(x cordinate val)
        we can have 2 points one at start and the other end.
        """
        left = 0
        right = len(height) - 1 
        most_water = 0 
        while left < right:
            h = min(height[left],height[right])
            l = right - left
            cur_water = l*h
            most_water = max(most_water,cur_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water

# attemp 3 code
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

        