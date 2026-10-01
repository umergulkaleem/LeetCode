class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #val and  count

        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1]+=1
                # print(stack,count,"count")
                
            else:
                stack.append([i,1])

            if stack[-1][1] == k:
                stack.pop()
        
        res = ""

        for char,count in stack:
            res+=char*count
        return res
        # print(stack)
        # return "".join(stack)
            
        