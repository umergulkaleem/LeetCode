class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        final = []
        came = False
        curr = ""
        dic = {}
        for i ,j in knowledge:
            dic[i] = j
        # print(dic)
        for i in s:
            if i !="(" and i !=")":

                curr+=i
            # print(curr)
            if i == "(" :
                came = True
                final.append(curr)
                curr = ""
            if came and i == ")":
                came = False
                if curr in dic:
                    word = dic[curr]
                else:
                    word = "?"
                final.append(word)
                curr = ""
        final.append(curr)
        if final[0] == "":
            final.pop(0)
        if final[-1] == "":
            final.pop(-1)
        # print(final)
        return "".join(final)

        