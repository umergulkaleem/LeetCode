class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # nums = sorted(nums)
        # arr = []
        # i = 0
        # print(nums)
        # while  i <len(nums)-1:
        #     first = nums[i]

        #     l,r=0,len(nums)-1
        #     new = float("inf")
        #     print(first,"first")
        #     while l<=r:
                
        #         mid = l+(r-l)//2
        #         second = nums[mid]
        #         print(second,"second")
        #         print(abs(first-second),"value")
        #         if abs(first-second)<new and mid !=i :

        #             new = abs(first-second)
        #             r = mid-1
        #         else:
        #             l = mid+1

        #     arr.append(new)
        #     # p-=1
        #     i+=1
        #     # if p==0:
        #     #     break

        # arr.sort()
        # print(arr)
        # res = float("-inf")
        # for i in range(p):
        #     res = max(res,arr[i])
        #     print(arr[i])
        # return res

        if p  ==0:
            return 0
        nums.sort()

        def check(n):
            i = 0
            count = 0
            while i<len(nums)-1:
                first = nums[i]
                second = nums[i+1]
                if abs(first-second) <= n:
                    count+=1
                    i+=2
                else:
                    i+=1
                if count == p:
                    return True
            return False
        
        l,r = 0,10**9
        res = 10**9
        while l<=r:
            mid = l+(r-l)//2

            if check(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
