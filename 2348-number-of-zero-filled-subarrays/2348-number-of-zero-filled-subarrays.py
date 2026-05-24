class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0
        count = 0

        for i in nums:
            if i ==0:
                count+=1
            else:
                count = 0

            res+=count
        return res


        # cont = 0
        # total = 0
        # hashmap = {}
        # subarray = []
        # for i in nums:
        #     if i ==0:
        #         subarray.append(i)
        #     else:
        #         subarray = []
        #     if len(subarray) not in hashmap:
        #         hashmap[len(subarray)] = 1
        #     else:
        #         hashmap[len(subarray)] +=1
        #     print(subarray,"subarray")
        #     print(hashmap,"hashmpa")
        # total = 0

        # for i in hashmap.values():
        #     total+=i
        # return total
            









        #     if cont>0:
        #         total+=1
        #     if i ==0 :
        #         total +=1
        #         cont+=1
        #     else:
        #         cont = 0
        #     print(total,"at",i)
        # print(total)
        