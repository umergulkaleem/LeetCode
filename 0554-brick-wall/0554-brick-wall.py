class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap = {0:0}

        for i in wall:
            total = 0
            for j in i[:-1]:
                total +=j
                gap[total] = 1+gap.get(total,0)
        return len(wall) - max(gap.values())