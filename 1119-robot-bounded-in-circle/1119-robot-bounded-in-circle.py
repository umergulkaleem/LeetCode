class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0
        # south = 0
        # east  = 0
        # west = 0
        # active = [north,west,south,east]
        # count = 0
        # for i in instructions:
        #     if i =="G" :
        #         active[count]+=1
        #     elif i == "L":
        #         count+=1
        #     elif i == "R":
        #         count-=1
        # print(active)
        # if active[0]>0 or active[2]>0:
        #     if active[0] == active [2] or active[0]==1 or active[2] == 1:
        #         print(active[2])
        #         return True
        # if active[1]>0 or active[2]>0:
        #     if active[1] == active[3] or active[1]==1 or active[3] == 1:
        #         return True
        # else:
        #     return False

        #` Directions in order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Start at origin and facing North (index 0 in directions)
        x = y = 0
        dir_idx = 0
        
        for inst in instructions:
            if inst == 'G':
                dx, dy = directions[dir_idx]
                x += dx
                y += dy
            elif inst == 'L':
                dir_idx = (dir_idx - 1) % 4  # Turn left: counter-clockwise
            elif inst == 'R':
                dir_idx = (dir_idx + 1) % 4  # Turn right: clockwise
        
        # Either returned to origin or not facing North
        return (x == 0 and y == 0) or dir_idx != 0

        