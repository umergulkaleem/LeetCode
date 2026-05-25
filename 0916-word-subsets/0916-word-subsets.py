class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for i in words2:
            tempmap = Counter(i)
            for c,cnt in tempmap.items():
                hashmap[c] = max(hashmap[c],cnt)
        print(hashmap)
        res = []
        for i in words1:
            tempmap  = Counter(i)
            ok = True
            for c,cnt in hashmap.items():
                if tempmap[c]<cnt:
                    ok = False
                    break
            if ok:
                res.append(i)
                

        return res