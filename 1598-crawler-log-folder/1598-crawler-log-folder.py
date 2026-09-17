class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for i in range(len(logs)):
            if len(stack)== 0 and logs[i]  == "../":
                continue
            if logs[i] == "./" or logs[i] == ",":
                continue
            if stack and logs[i] == "../":
                stack.pop()
            else:
                stack.append(logs[i])
            print(stack)
        
        return len(stack)        