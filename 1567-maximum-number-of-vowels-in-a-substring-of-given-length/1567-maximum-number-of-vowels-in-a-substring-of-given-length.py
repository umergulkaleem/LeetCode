class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # vowel = 'aeiou'
        # maxcount = 0
        # for i in range(len(s)):
        #     count = 0
        #     if s[i] in vowel:
        #         for j in range(i,min(i + k, len(s))):
        #             if s[j] in vowel:
        #                 count+=1
        #                 print(count,"at",i)
        #         maxcount =max(maxcount,count)
        # return maxcount

        vowels = set('aeiou')
        count = 0
        maxcount = 0

        # count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxcount = count

        # slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            maxcount = max(maxcount, count)

        return maxcount
        