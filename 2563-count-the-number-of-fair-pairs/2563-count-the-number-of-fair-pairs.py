class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # p1,p2 = 0,0
        # count = 0
        # pairs = []
        # nums = sorted(nums)
        # print(nums)
        # while p1<len(nums)-1:
        #     for i in range(abs(nums[p1]-lower),abs(nums[p1]-upper)):
        #         k = i

        #         l = p1+1
        #         r = len(nums)-1
        #         while l<=r:
        #             mid = l+(r-l)//2

        #             if nums[mid] == k:
        #                 count+=1
        #                 pairs.append((p1,mid))
        #                 l = mid+1
                        
        #             elif nums[mid]>k:
        #                 r  = mid-1
        #             else:
        #                 l = mid+1
        #     p1+=1
        # print(pairs,count)



        def helper(l,r,target):

            while l<=r:
                mid = l+(r-l)//2

                if nums[mid]>=target:
                    r = mid-1
                else:
                    l=mid+1

            return r


        
        res = 0
        nums.sort()

        for i in range(len(nums)):
            low = lower-nums[i]
            up = upper - nums[i]

            res +=(
                helper(i+1,len(nums)-1,up+1)-
                helper(i+1,len(nums)-1,low)
            )
        return res



        