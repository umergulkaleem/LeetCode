class Solution:
    def sortVowels(self, s: str) -> str:
        index = []
        invowel = []
        vowel = "aeiouAEIOU"
        count = 0
        for i in range(len(s)):
            if s[i] in vowel:
                index.append(i)
                invowel.append(s[i])
        print(index,"index")
        invowel.sort()

        s= list(s)

        for k in index:
            s[k] = invowel[count]
            count += 1

        s = "".join(s)
        return s

            
        