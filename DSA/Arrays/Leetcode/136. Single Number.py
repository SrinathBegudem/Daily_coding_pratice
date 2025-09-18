class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR is associative, commutative, and self-canceling (x ^ x = 0), you can reorder and cancel pairs.
        even if you do sequentially the end ans will be same as arrange all of them together reordering and canceling 
        properties :
        x^x = 0
        x^y = cal binary of x and y and then add the binary and then convert it into digits 
        0^0 =0
        1^1 = 0
        1^0 = 1
        0^1 = 1
        """
        #so start with zero and just do sequentailly for intuition think all nums in arr xor it adn the left over num will be the one which will be left off.
        res = 0
        for num in nums:
            res ^= num
        return res
