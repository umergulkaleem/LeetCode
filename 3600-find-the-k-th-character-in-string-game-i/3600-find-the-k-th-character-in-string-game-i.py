class Solution:
    def kthCharacter(self, k: int) -> str:

        # def helper(word,k,n):
        #     if len(word) >= k:
        #         return word[k-1]
        #     print(word,"start")
        #     asci = ord(word[n])
        #     nextword = chr(asci+1) + chr(asci+2)
        #     print(nextword,"nextword")
        #     word+=nextword
        #     print(word)
        #     helper(word,k,n+1)

        # word = "a"
        # # print(asci)
        # # print(chr(asci))
        # n=0

        # helper(word,k,n)
        def helper(word, k):
            if len(word) >= k:
                return word[k - 1]
            changed_word = ""
            for i in range(len(word)):
                rec = ord(word[i])
                print(rec,"rec")
                changed_word += chr(rec+1)
                print(changed_word)
            print(changed_word,"full changed")
            word+=changed_word

                


           
            

            return helper(word, k)

        # Initial call
        word = "a"
        result = helper(word, k)
        return result

        