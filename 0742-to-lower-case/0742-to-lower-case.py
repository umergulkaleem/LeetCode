class Solution:
    def toLowerCase(self, s: str) -> str:
        result =""
        for i in range(len(s)):
            changed = ord(s[i])
            print(changed,"in main")
            if changed<=90 and changed>=65:
                changed+=32
                print(changed)
                character = chr(changed)
                print(character)

                result+=  character
            else:
                result +=s[i]
        return result
