class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countud = 0
        countlr = 0
        for i in moves:
            if i == "U":
                countud+=1
            elif i == "D":
                countud-=1
            elif i == "R":
                countlr+=1
            elif i == "L":
                countlr-=1
        if countud == 0 and countlr == 0:
            return True
        else:
            return False
            
        