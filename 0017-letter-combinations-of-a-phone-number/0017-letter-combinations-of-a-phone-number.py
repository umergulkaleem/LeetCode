class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        # result = [""]

        # for digit in digits:
        #     letters = phone_map[digit]
        #     temp = []
        #     for prefix in result:
        #         for letter in letters:
        #             temp.append(prefix + letter)
        #     result = temp

        # return result
        def back(combination,next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    back(combination+letter,next_digits[1:])
        output = []
        back("",digits)
        return output
        