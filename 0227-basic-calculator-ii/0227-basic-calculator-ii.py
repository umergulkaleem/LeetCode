class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        if all(i not in "/*-+" for i in s):
            return int(s)
            
        tmp = ""
        for i in s:
            if i == " ":
                continue

            if i in "/*-+":
                stack.append(tmp)
                stack.append(i)
                tmp = ""
            else:
                tmp += i

        if tmp:
            stack.append(tmp)
        # print(stack)
        # print(type(/w))

        i = 1

        while i<len(stack)-1:
            # print(i,"i")
            # print(stack[i])
            if stack[i] == "*" or stack[i] == "/":

                first = int(stack[i+1])
                second = int(stack[i-1])
                # print(first,second)
                if stack[i] == "*":
                    new = second * first
                else:
                    new = second / first
                # print(new,"new")
                stack[i - 1:i + 2] = [new]
            else:
                i+=1
        

        result = int(stack[0])

        i = 1
        while i<len(stack):
            op = stack[i]
            right = int(stack[i+1])
                
            if op == "+":
                result += right
            else:
                result -= right
            i+=2
        return result