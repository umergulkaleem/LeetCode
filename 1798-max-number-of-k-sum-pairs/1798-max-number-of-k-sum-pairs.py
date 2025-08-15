class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        point1= 0
        point2 = len(nums)-1
        count = 0
        while point1<point2:

            sum1 = nums[point1]+nums[point2]
            print(sum1,"sum")
            print(point1,"1")
            print(point2,"2")
            if sum1==k:
                count+=1
                point1+=1
                point2-=1
            elif sum1 < k:    #gpt help here
                point1 += 1
            else:
                point2-=1
        return count
        