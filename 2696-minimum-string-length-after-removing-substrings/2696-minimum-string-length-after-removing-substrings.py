class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack:
                prev = stack[-1]
            curr = s[i]
            print(stack)
            if stack and prev == "A" and curr =="B":
                stack.pop()
              
            elif stack and prev == "C" and curr  == "D":
                stack.pop()
            
            else:
                stack.append(curr)
        return len(stack)

        