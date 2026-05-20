class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap  ={}
        for i in s1.split(" "):
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i in s2.split(" "):
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
            
        
        print(hashmap)
        res = []
        for i in hashmap:
            if hashmap[i]==1:
                res.append(i)
        return res

        