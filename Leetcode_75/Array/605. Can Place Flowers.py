class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # time, space = o(n), o(1)
        # base condition(edge condition): if n == 0 return right away  
        if n == 0: return True
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:# check if cur plot is 0
                # lets check left is out of bounds or 0 
                leftSide = i-1 < 0 or flowerbed[i-1] == 0
                # lets check right is out of bounds or 0 
                rightSide = i + 1 >= len(flowerbed) or flowerbed[i+1] == 0
                if leftSide and rightSide:
                    flowerbed[i] = 1
                    n -= 1
                if n == 0: return True # early cut off 
        return False


        