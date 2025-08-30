class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack = []
        # count = 0
        # def helper(count,stack):
        #     if count ==len(s)-1:
        #         return stack
        #     if s[count] == "]":

        #     stack +=s[count]
        #     print(stack)
        #     helper(count+1,stack) 
        # stack = []
        # helper(0,stack)
        stack = []
        num = 0
        cur = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)   # handle multi-digit numbers
            elif ch == "[":
                stack.append(cur)
                stack.append(num)
                cur = ""
                num = 0
            elif ch == "]":
                repeat = stack.pop()
                prev = stack.pop()
                cur = prev + cur * repeat
            else:
                cur += ch

        return cur    
            

        