class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        new = ''
        for ch in order:
            if ch in hashmap:
                new+=ch*hashmap[ch]
                del(hashmap[ch])
        for ch in hashmap:
            new+=ch*hashmap[ch]
        return new


