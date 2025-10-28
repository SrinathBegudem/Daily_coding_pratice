class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        The inuition here is 
        -when we are at paticular indx we check leftside and right side to plant a flower
        - left side is True if there are no flowers to the left or the left side is less than 0 
        - right side is True if there are no flowers to the right side of indx or right side is out of index

        """
        # lets loop over the flower bed and see if we can plan n flowers
        for i in range(len(flowerbed)):
            # lets check left if its neihter less than 0 or the left side is not eq to 1 so we can plant 
            leftSide = True if (i-1 < 0) or (flowerbed[i-1] != 1) else False
            # simialrly to right side we check if right side is out of index or right side has not fower so we plant 
            rightSide = True if (i+1 >= len(flowerbed)) or (flowerbed[i+1] != 1) else False
            # check if the cur index is not eq to 1 ( no flower already present) and check if left and right is empty
            if flowerbed[i] != 1 and leftSide and rightSide:
                # if yes plant a flower 
                flowerbed[i] = 1
                #and reduce the total no of flower left 
                n -= 1
        # if all the plants are sucesfully planted then n ==0 and if there are more spaces left n can go negative which is also valid. or goal is to check only if n plants can be planted 
        return n <= 0