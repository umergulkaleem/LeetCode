class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        "when the stack start that is a when the stack empty b store in list"

        stack= []
        remove = []
        a,b = 0,0
        for i,p in enumerate(s):
            if stack and p == ")":
                stack.pop()
                if not stack:
                    remove.append(i)
            
            else:
                if not stack:
                    remove.append(i)
                stack.append(p)
            # print(remove,"at",stack)

        for i in reversed(remove):
            s = s[:i] + s[i+1:]
            # print(s,"after removing",i)
        return s

        

            
