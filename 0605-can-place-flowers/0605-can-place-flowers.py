class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        # if len(flowerbed)==1:
        #     if flowerbed[0] == 0 and n==1:
        #         return True

        #     if n==0:
        #         return True

        # last  = flowerbed[0]
        # for i in range(1,len(flowerbed)):
        #     curr = flowerbed[i]
        #     if i<len(flowerbed)-1:
        #         next1 = flowerbed[i+1]
        #     if last==0 and curr ==0 and next1 == 0 or i==1 and last ==0:
        #         n-=1
        #         flowerbed[i] = 1
        #     if n == 0 :
        #         return True
        
        #     last=flowerbed[i]
        # return False
        length = len(flowerbed)
    
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                        
        return n == 0

        