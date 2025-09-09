class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        
        # for i in range(len(temperatures)):
        #     found = False
        #     days = 0

        #     for k in range(i+1,len(temperatures)):
        #         days+=1
        #         if temperatures[k]>temperatures[i]:
        #             stack.append(days)
        #             found = True
            
        #             break
        #     if not found:
        #         stack.append(0)
        # return stack
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than the one at stack's top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res
        