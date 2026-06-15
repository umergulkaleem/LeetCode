class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        # res = 0

        # hashset = set(ideas)

        # for i in range(len(ideas)):
        #     first = ideas[i]
        #     for j in range(len(ideas)):
        #         if i == j:
        #             continue
        #         second = ideas[j]
        #         # print(first)
        #         # print(second)
        #         first = list(first)        
        #         second = list(second)        
        #         #now swap the frist letter of each words
        #         first[0],second[0] = second[0] ,first[0]
        #         # print(first)
        #         # print(second)
        #         first = "".join(first)        
        #         second = "".join(second)   
        #         if first not in hashset and second not in hashset:
        #             print(first)
        #             print(second)
        #             res+=1
        # return res
        
        hashset   = defaultdict(set)
        for w in ideas:
            hashset[w[0]].add(w[1:])
        res = 0

        for char1 in hashset:
            for char2 in hashset:
                if char1 == char2:
                    continue
                
                intersect = 0
                for w in hashset[char1]:
                    if w in hashset[char2]:
                        intersect +=1
                distinct1 = len(hashset[char1])-intersect
                distinct2 = len(hashset[char2])-intersect
                res +=distinct1*distinct2
        return res