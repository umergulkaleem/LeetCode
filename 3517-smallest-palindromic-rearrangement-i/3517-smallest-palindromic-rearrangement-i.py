class Solution:
    def smallestPalindrome(self, s: str) -> str:

        hmap = Counter(s)
        
        new = []
        odd = ""
        for i in sorted(hmap.keys()):
            new.append(i*(hmap[i]//2))
            if hmap[i] % 2 ==1:
                odd = i
        return "".join(new) + odd + "".join(reversed(new))

                

        