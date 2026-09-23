class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        stack = []
        p0  = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] ==popped[p0]:
                # print(stack)
                stack.pop()
                p0+=1
        return len(stack) == 0
            
        