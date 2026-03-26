class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # new = triplets.copy()

        # for i in range(len(triplets)):
        #     found = False
        #     for j in range(len(triplets[i])):
        #         # print(triplets[i][j])

        #         # print(target[j],"target")
        #         if triplets[i][j] == target[j] and triplets[i][j] < target[j] :
        #             found = True
        #             # print("found,at",triplets[i][j])
        #     if  found == False:
        #         new.pop(i)
        #     # print(new,"new")
        # count = 0
        # while count!=len(target):
        #     found = False
        #     for i in new:
        #         print(i[count],"at")
        #         print(target[count],"check")
        #         if i[count]==target[count]:
        #             found = True
        #     print(found,"found")
        #     if found == False:
        #         return False
        #     count+=1

        # return True

        good = set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2] :
                continue

            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good)==3