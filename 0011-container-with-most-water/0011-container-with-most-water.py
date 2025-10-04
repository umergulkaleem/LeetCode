class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area  =0
        while left<right :
            left_hand = height[left]
            right_hand = height[right]
            area = min(left_hand,right_hand)*(right-left)
            max_area = max(area,max_area)
            if left_hand<right_hand:
                left+=1
            else:
                right-=1
        return max_area

        