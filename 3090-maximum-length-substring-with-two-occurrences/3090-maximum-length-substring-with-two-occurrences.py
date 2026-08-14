class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        l=0
        hmap={i:0 for i in set(s)}
        print(hmap)
        res=0
        win =""
        for r in range(len(s)):
            hmap[s[r]]+=1
            while max(hmap.values()) > 2:
                hmap[s[l]]-=1
                print("new",hmap)
                l+=1
            res = max(res,r-l+1)
        return res