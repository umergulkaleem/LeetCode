class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newlist = []
        sum1=0
        for op in operations:
            if op == "C":
                if newlist:
                    newlist.pop()
            elif op == "D":
                if newlist:
                    newlist.append(2 * newlist[-1])
            elif op == "+":
                if len(newlist) >= 2:
                    newlist.append(newlist[-1] + newlist[-2])
            else:
                newlist.append(int(op))
        for j in newlist:
            sum1 +=j
        return sum1
        

        