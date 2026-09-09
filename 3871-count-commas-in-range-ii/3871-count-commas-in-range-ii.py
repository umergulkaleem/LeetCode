class Solution:
    def countCommas(self, n: int) -> int:

        tmp = 0
        res = 0
        new = n
        grp= []
        curr = []
        while new:
            curr .append(new%10)
            # print(curr)
            tmp+=1
            if tmp==3:
                # print("in")
                grp.append(curr)
                tmp = 0
                curr = []
            new =new//10
        # print(grp)
        if curr:
            grp.append(curr)

        commas = len(grp)-1
        power = 1000
        for i in range(commas):
            res += n-power+1
            power *=1000
        return res
        