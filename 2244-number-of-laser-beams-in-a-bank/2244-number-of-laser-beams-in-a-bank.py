class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        initial = 0 
        for i in bank:
            print("at",i)
            if "1"not in i:
                continue
            if initial != 0:
                next = i.count("1")
                total +=initial*next
                print(total,"total")
            print(initial,"in")
            initial = i.count("1")
        return total

        