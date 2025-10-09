class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append((0,temperatures[0]))
        for i, temp in enumerate(temperatures[1:],start=1):
            while stack and temp > stack[-1][1]:
                stackI,stackT = stack.pop()
                diff = i - stackI
                res[stackI] = diff
            stack.append((i,temp))
        return res
