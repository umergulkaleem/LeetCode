class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        new = n + 1

        while True:
            s = str(new)
            balanced = True  
            
            for digit in s:
                count = s.count(digit)
                if count != int(digit):
                    balanced = False
                    break
            
            if balanced:
                return new
                break
            else:
                new += 1
                    

            

        