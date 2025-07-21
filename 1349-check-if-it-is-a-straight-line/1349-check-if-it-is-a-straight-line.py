class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # Calculate initial slope
        if (x2 - x1) == 0:
            m = None  # vertical line
        else:
            m = (y2 - y1) / (x2 - x1)

        for i in range(1, len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]

            if (x2 - x1) == 0:
                m1 = None
            else:
                m1 = (y2 - y1) / (x2 - x1)

            if m1 != m:
                return False

        return True

        