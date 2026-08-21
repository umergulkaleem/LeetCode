class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:


        max_limit = min(coins)*k
        # arr = []
        # for i in range(len())
        def findcount(coins,mid):
            cnt = 0
            n = len(coins)
            midones = 1<<n
            for i in range(1,midones):
                setbitslcm = 1

                for j in range(n):
                    if i & (1<<j):
                        setbitslcm = lcm(setbitslcm,coins[j])
                
                if i.bit_count()%2==1:
                    cnt+=mid//setbitslcm
                else:
                    cnt-=mid//setbitslcm
            return cnt

        l , r =  0,max_limit
        ans =0
        while l<=r:
            mid = (l+r)//2
            count = findcount(coins,mid)
            print(count)
            if count<k:
                l = mid+1
            else:
                ans = mid
                r = mid-1        
        return ans







            
        