class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ""
        stack = []
        vowels ="aeiouAEIOU"

        for char in s:
            if char in vowels:
                stack.append(char)
        for char in s:
            if char in vowels:
                result = result+stack.pop()
            else:
                result = result+char            
        return result