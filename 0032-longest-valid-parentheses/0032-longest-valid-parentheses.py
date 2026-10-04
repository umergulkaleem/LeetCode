class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s)<1:
            return 0
        tmp = 0
        longest = 0
        i = 0
        stack = []
        last_invalid_closing  = -1
        

        while i < len(s):
            curr = s[i]
            
            if  curr == ")":

                if stack:
                    stack.pop()
                    if stack:
                        tmp = i - stack[-1]
                    else:
                        tmp = i-last_invalid_closing
                else:
                    last_invalid_closing = i
                longest = max(tmp,longest)

            else:
                stack.append(i)
           
            i+=1
        return longest          
        
        