class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # total = 0
        # for i in range(len(stones)):
        #     point = 0
        #     # if i % 2 ==0:
        #     while point < len(stones) and stones[point] + total % 3 ==0:
        #         point+=1
        #     print(point,"at",i)

        #     total +=stones[point]
        #     if total % 3 ==0 and i % 2 !=0:
        #         return True
        #     elif  total % 3 == 0 and i % 2 == 0:
        #         return False
        #     if point == len(stones)-1:
        #         return False
        #     stones.pop(point)
        # return True
        

        hmap = Counter(x%3 for x in stones)
        print(hmap)
        # name  = ""
        # total = 0
        # for i in range(len(stones)):
        #     if i % 2 ==0:
        #         name = "Alice"
        #     else:
        #         name  = "Bob"
        #     if hmap[2]>0 and (total + 2) % 3 !=0:
        #         hmap[2]-=1
        #         total = (total+2)%3
        #     elif hmap[1]>0 and (total+ 1) % 3 !=0:
        #         total = (total+1)%3
        #         hmap[1]-=1
        #     elif hmap[0]>0:
        #         hmap[0]-=1
        #     else:
        #         return name == "Bob"
        # return False
        count0 = hmap[0]
        count1= hmap[1]
        count2 = hmap[2]

        if count1 == 0 and count2== 0:
            return False

        if count0 % 2 == 0:
            return count1>0  and count2>0

        return abs(count1 - count2) >2

            


        
        