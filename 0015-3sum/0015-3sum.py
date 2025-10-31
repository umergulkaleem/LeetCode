class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        for i in range(len(nums)-2):

            point1 = i+1
            point2 = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while point1 <point2:
                res = nums[i]+nums[point1]+nums[point2]
                
                if res == 0:
                    temp = [nums[i],nums[point1],nums[point2]]
                    print(temp,"temp","at",i)
                    
                    final.append(temp)
                    while point1<point2 and nums[point1]  == nums[point1+1]:
                        point1+=1
                    while point1<point2 and nums[point2] == nums[point2-1]:
                        point2-=1
                    point1+=1
                    point2-=1
                elif res<0:
                    point1+=1
                else:
                    point2-=1
        return final

                    



        