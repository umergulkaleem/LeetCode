class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n =len(s)
        # copy = Counter(s)

        # total = math.factorial(n)
        # tmp = 0
        
            
        # while tmp<26:
        #     arr = []
        #     return1 = False
        #     for i  in range(n-1,-1,-1):
        #         if copy[chr(ord(target[i])+tmp)] > 0:
        #             arr.append(chr(ord(target[i])+tmp))
        #             copy[chr(ord(target[i])+tmp)]-=1
        #             return1 = True
        #         else:
        #             arr.append(s[i])
        #     if return1 and target< "".join(arr):
        #         return "".join(arr)
        #     tmp+=1


        for i in range(n-1,-1,-1):

            count =Counter(s)
            possible = True


            for j in range(i):

                if count[target[j]] == 0:
                    possible = False
                    break
                count[target[j]]-=1

            if not possible:
                continue

            for tmp in range(1,26):

                ch = chr(ord(target[i])+tmp)

                if count[ch]>0:

                    count[ch]-=1
                    result = target[:i]+ch

                    for c in sorted(count):
                        result+=c*count[c]

                    return result
        return ""



            
                    
                





        