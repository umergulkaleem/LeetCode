class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length = 0 
        # found = []
        # max_len = 0
        # for i in s:
        #     if i not in found :
        #         print(i,"not")
        #         found.append(i)
        #         length+=1
        #         print(length,"len")

        #     else: 
        #         found = []
        #         print(length,"in else len")
        #         max_len = max(max_len,length)
        #         length = 0
        # return max_len
        length = 0
        found = []
        max_len = 0

        for i in s:
            if i not in found:
                found.append(i)
                length += 1
                max_len = max(max_len, length)
            else:
                # remove characters until the duplicate is gone
                dup_index = found.index(i)
                found = found[dup_index+1:] + [i]
                length = len(found)
        return max_len
            
        