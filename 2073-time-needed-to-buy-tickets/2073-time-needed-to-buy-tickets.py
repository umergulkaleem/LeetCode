class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # ans = 0
        # count = tickets[k]
        # new = tickets.copy()
        # while count>0:
        #     print(ans,"ans before")

        #     for i in range(len(new)):
        #         if len(new) == 1:
        #             return ans
        #         if new[0] == 0:
        #             new.pop(0)
        #         else:
        #             new[0]-=1
        #             new.append(new[0])
        #             new.pop(0)
        #         print(new,"nums")
        #         ans+=1
        #     count-=1
        #     print(ans,"ans")
        # return ans

        ans = 0

        for i in range(len(tickets)):
            if i<=k:
                ans+=min(tickets[i],tickets[k])
            else:
                ans+=min(tickets[i],tickets[k]-1)
        return ans
