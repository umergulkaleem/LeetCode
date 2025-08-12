class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        point1 = 0
        point2 = len(height)-1
        maxheight = 0
        while point1<point2:
            m = min(height[point1] , height[point2])*(point2-point1)
            
            if height[point1] > height[point2]:
                point2-=1
            else:
                point1+=1
            maxheight = max(m,maxheight)
            print(maxheight)
        return maxheight
            

        