class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleastk(k):
            vowel = "aeiou"

            res = 0
            con = 0
            l  = 0
            tmp = defaultdict(int)
            for r in range(len(word)):
                curr = word[r]
                if curr not in vowel:
                    con+=1
                else:
                    tmp[curr]+=1
                # print(con,"con",l,"l")
                while len(tmp) == 5  and con >= k:
                    res += len(word)-r
                    new = word[l]
                    if new not in vowel:
                        con-=1
                    else:
                        tmp[new]-=1
                    if tmp[new] == 0:
                        tmp.pop(new)
                    l+=1
                # print(tmp)
               
            return res
        return atleastk(k)-atleastk(k+1)
        