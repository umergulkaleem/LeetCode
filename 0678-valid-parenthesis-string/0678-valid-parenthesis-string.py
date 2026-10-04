class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        stack2 = []
        for i in range(len(s)):
            curr = s[i]
            # print(curr)
            # print(stack)
            # print(stack2)
            if curr == ")":
                if stack:
                    stack.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False 
            else:
                if curr == "(":
                    stack.append(i)
                else:
                    stack2.append(i)
       
        while stack and stack2:
            if stack[-1] < stack2[-1]:
                stack.pop()
                stack2.pop()
            else:
                return False

        return not stack


