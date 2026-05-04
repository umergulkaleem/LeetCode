class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # div= []
        # for i,j in rectangles:
        #     ans = i /j
        #     div.append(ans)

        res = 0
        hashmap  = {}
        for w,h in rectangles:

            g = gcd(w,h)

            key = (w//g,h//g)
            # print(hashmap,"hashmap")
            if key in hashmap:
                res += hashmap[key]
                hashmap[key] += 1
            else:
                hashmap[key] = 1

        return(res)




















            # for indexj,j in enumerate(rectangles):
        
            #     tmp1 = j[0]/j[1]
            #     if index== indexj:
            #         continue
            #     if tmp == tmp1:
            #         res+=1
        # return int(res/2)


        