class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                stackT,stacki = stack.pop()
                result[stacki] = (i-stacki)
            stack.append([t,i])
        return result
        