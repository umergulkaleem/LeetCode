class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        res = 0
        l = 0

        hashmap = Counter(s)
        if len(hashmap)<3 and k>0:
            return -1
        for i in hashmap.values():
            if i<k:
                return -1
        for r in range(len(s)):
            curr = s[r]

            hashmap[curr]-=1
            # print(hashmap)
            while any(count < k for count in hashmap.values()):
                hashmap[s[l]]+=1
                l+=1
            # print(hashmap,"later")
            # print("valid window",l,r)
            res = max(res,r-l+1)
        
        return len(s)-res
        
