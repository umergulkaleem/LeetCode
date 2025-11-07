class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dif = inf
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):

            point1 =i+1
            point2 = len(nums)-1

            while point1<point2:
                dif = nums[i]+nums[point1]+nums[point2]
                res.append(dif)
                if dif<target:
                    point1+=1
                else:
                    point2-=1
        return min(res, key=lambda x: abs(x - target))