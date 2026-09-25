class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = []

        newpath = path.replace("/"," ")
        newpath = newpath.split(" ")
        # print(newpath)

        for i in newpath:
            if i !="":
                tmp.append(i)
            # print(tmp,"after",i)
        
        stack = []

        for i in tmp:
            i.replace(" ","")
            # print(i,"i")
            if i == ".":
                continue
            if stack and i == "..":
                # print("in")
                if len(stack)>=2:
                    stack.pop()
                    stack.pop()
            else:
                if i !="..":
                    stack.append("/")
                    stack.append(i)
        if not stack:
            return "/"
                
            # print(stack)
        # if stack and stack[-1] == "..":
        #     stack.pop() 
        return "".join(stack)
        

            

        