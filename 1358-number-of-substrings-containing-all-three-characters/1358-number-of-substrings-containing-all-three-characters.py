class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        # mainmap = Counter(s)
        # for i in s:
        #     mainmap[i]-=1
        #     print(mainmap)
        #     if mainmap["a"]>0 and mainmap["b"]>0 and mainmap["c"]>0:
        #         res+=1
        # return res

        curr_win = {"a":0,"b":0,"c":0}
        l = 0
        # curr_win.append(s[l])
        for r in range(len(s)):
            # curr_win.append(s[r])
            curr_win[s[r]]+=1
            # print(curr_win)
            while curr_win["a"]>0 and curr_win["b"]>0 and curr_win["c"]>0:
                # print("in")
                res+=len(s)-r
                curr_win[s[l]]-=1
                l+=1
        return res
            


        