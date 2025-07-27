class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        print(freq)
        count=0
        if len(freq)==1:
            print("lenght one")
            value = next(iter(freq.values()))
            return value
        has_one = False
        for i in freq.values():
            if i % 2==0:
                
                count+=i
            else:
                count+=i-1
            if i % 2 == 1:
                has_one = True

        if has_one:
            count+=1
        return count
            