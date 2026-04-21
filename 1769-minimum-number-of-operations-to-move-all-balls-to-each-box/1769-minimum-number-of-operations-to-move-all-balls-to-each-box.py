class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        res = [0] * len(boxes)
        move , ball = 0,0
        for i in range(len(boxes)):

            res[i]+= move+ball

            move = move+ball
            ball += int(boxes[i])
        move , ball = 0,0
        for i in reversed(range(len(boxes))):

            res[i] += move+ball

            move = move+ball
            ball += int(boxes[i])
        return res

        

        