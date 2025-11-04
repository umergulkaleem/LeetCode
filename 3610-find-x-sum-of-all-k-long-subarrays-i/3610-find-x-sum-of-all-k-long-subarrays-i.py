class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            
            temp  = nums[i:k+i]
            print(temp,"temp")
            

            freq = Counter(temp)
            freq = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)
            print(freq,"freq")
            newfreq = freq[:x]
            # print(newfreq ,"freq new")
            total  = 0

            for f,s in newfreq:
                total +=f*s
               
            print(total,"total")
            ans.append(total)
        return ans

                

        